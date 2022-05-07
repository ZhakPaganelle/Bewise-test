"""Module for working with db"""

from collections.abc import AsyncGenerator

from sqlmodel import SQLModel

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


engine = create_async_engine(
    'postgresql+asyncpg://bewise:bewise@postgres/bewisedb',
    echo=True,
    future=True,
)


async def init_db():
    """Creates all tables"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession | AsyncGenerator:
    """Returns session connection to the db"""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
