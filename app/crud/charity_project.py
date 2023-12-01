"""Модуль для класса CRUD операций модели CharityProject."""


from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectUpdate,
)


class CRUDCharityProject(
    CRUDBase[CharityProject, CharityProjectCreate, CharityProjectUpdate]
):
    """Класс CRUD операций для модели CharityProject."""

    async def get_project_by_name(
        self,
        session: AsyncSession,
        project_name: str,
    ) -> Optional[int]:
        """Чтение объекта CharityProject по имени (поле name)."""
        db_project = await session.execute(
            select(CharityProject).where(CharityProject.name == project_name)
        )
        db_project = db_project.scalars().first()
        return db_project


charity_project_crud = CRUDCharityProject(CharityProject)
