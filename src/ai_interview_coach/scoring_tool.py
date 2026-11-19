from ai_interview_coach.answer_score import AnswerScore

class ScoringTool:
    def __init__(self, schema) -> None:
        self.SCORING_TOOL = {
            "type": "function",
            "function": {
                "name": "score_answer",
                "description": (
                    "Evaluate a candidate's interview answer on clarity "
                    "and correctness. Provide reasoning and feedback."
                ),
                "parameters": schema
            }
        }