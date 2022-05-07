"""API for parsing and saving questions"""
from fastapi import Depends, FastAPI

from sqlalchemy import func, desc
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from db import init_db, get_session
from models import Question
from questions_parser import get_questions

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    """Initialises tables for db"""
    await init_db()


@app.get("/hello/", response_model=str)
async def hello():
    """Test function"""
    return "Hello"


@app.post("/questions", response_model=Question)
async def add_questions(questions_num: int = 1, session: AsyncSession = Depends(get_session)):
    """Adds given number of questions to db"""
    if questions_num < 1:
        return await get_last_question(session)

    initial_questions_num = await get_questions_count(session)
    while (diff := await get_questions_count(session) - initial_questions_num) < questions_num:
        questions = [
            Question(**question).dict()
            for question in await get_questions(questions_num - diff)
        ]
        for question in questions:
            question.pop("id")
        await session.execute(insert(Question)
                              .values(questions)
                              .on_conflict_do_nothing())
        await session.commit()
    return await get_last_question(session)


async def get_questions_count(session: AsyncSession) -> int:
    """Returns amount of questions from the db"""
    req = (await session.execute(select(func.count()).select_from(Question))).scalar()
    return req  # type: ignore


async def get_last_question(session: AsyncSession) -> dict[str, str]:
    """Returns last questions from db"""
    req = (await session.execute(select(Question)  # type: ignore
                                 .order_by(desc(Question.id))
                                 .limit(1))).fetchone()["Question"]
    return req
