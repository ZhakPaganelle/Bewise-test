from datetime import datetime
from sqlmodel import SQLModel, Field


class QuestionBase(SQLModel):
    question: str
    answer: str


class Question(QuestionBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class QuestionRequest(SQLModel):
    questions_num: int = 1
