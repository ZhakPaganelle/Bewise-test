"""Models for API and db tables"""

from datetime import datetime
from sqlmodel import SQLModel, Field


class QuestionBase(SQLModel):
    """Initial class for questions"""
    question: str
    answer: str


class Question(QuestionBase, table=True):
    """Model that represents question in the db"""
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class QuestionRequest(SQLModel):
    """Model that is waited from user for requesting new questions"""
    questions_num: int = 1
