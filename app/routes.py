"""API for parsing and saving questions"""
from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import init_db, get_session
from models import Question, QuestionRequest

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/hello/", response_model=str)
async def hello():
    """Test function"""
    return "Hello"


@app.post("/questions")
async def add_questions(questions_num: int, session: AsyncSession = Depends(get_session)):
    question = Question(question='Да?', answer='Пизда')
    print(question.json())
    session.add(question)
    await session.commit()
    return {"test": "test"}
