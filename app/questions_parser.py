"""Module for parsing site with questions"""

import aiohttp

Question = dict[str, str | int]
URL = "https://jservice.io/api/random"


async def get_questions(count: int = 1) -> list[Question]:
    """Returns list with questions from site"""
    async with aiohttp.ClientSession() as session:
        async with session.get(URL, params={"count": count}) as resp:
            questions = await resp.json()
    return await parse_questions(questions)


async def parse_questions(questions: list[Question]) -> list[Question]:
    """Parses questions from the site preparing them for orm"""
    keys = ["question", "answer"]
    return [
        {key: question.get(key, "") for key in keys}
        for question in questions
    ]
