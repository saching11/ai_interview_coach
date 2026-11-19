import json
from ai_interview_coach.scoring_tool import ScoringTool
from ai_interview_coach.answer_score import AnswerScore

class InterviewSession:

    def __init__(self) -> None:
        self.INTERVIEW_SYSTEM_PROMPT_LEARNING = """
            You are an AI Interview Coach for ios developers with ~8 years of experience

            Your persona:
            - Professional and direct. Not warm or chatty.
            - You give honest scores. You do not inflate feedback to make candidates feel good.
            - You stay in the interviewer role for the entire session.

            Your Task:
            - Ask a question, keep it very short and simple
            - Don't repeat the same question again.
        """
        
        self.SYSTEM_ANSWER_CHECK_PROMPT = """
            You need to check the answer given by user for a question.
            Evaluate the answer step by step.
            Only respond with the json which gives answer scores
        """

        self.QUESTIONS_ASKED = []
        self.schema = AnswerScore.model_json_schema()
        self.scoring_tool = ScoringTool(self.schema)
    
    def ask_question(self, client) -> str:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {
                    "role":"system",
                    "content":self.INTERVIEW_SYSTEM_PROMPT_LEARNING + f" Questions which are already asked {self.QUESTIONS_ASKED}"
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content
    
    def send_answer_to_check(self, client, question, answer):
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {
                    "role":"system",
                    "content":self.SYSTEM_ANSWER_CHECK_PROMPT
                },
                {
                    "role":"user",
                    "content":f"Question : {question} \n Answer : {answer}"
                }
            ],
            tools=[self.scoring_tool.SCORING_TOOL],
            tool_choice="auto"
        )


        if response.choices[0].message.tool_calls[0].function.name == "score_answer":
            self.score = self.validate_answer(json.loads(response.choices[0].message.tool_calls[0].function.arguments))

        return self.score
    
    def validate_answer(self, answer):
        try:
            answer_score = AnswerScore(**answer)
            return answer_score
        except ValidationError as e:
            raise ValueError(f"Model return invalid scoring json {e}")

    

    


