from pydantic import BaseModel, Field, ValidationError

class AnswerScore(BaseModel):
    reasoning: str = Field(
        description="Give reason behind the score in maximum 3 sentences"
    )
    clarity: int = Field(
        ge=1,
        le=5,
        description="Check the clarity of the answer and give a score between 1-5"
    )
    correctness: int = Field(
        ge=1,
        le=5,
        description="Check the correctness of the answer and give a score between 1-5"
    )
    feedback: str = Field(
        description="Give feedback on the answer in maximum 3 sentences"
    )

