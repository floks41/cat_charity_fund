"""Модуль для подключения роутеров эндпоинтов работы с пользователями."""


from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@router.delete('/users/{id}', tags=['users'], deprecated=True)
def delete_user(id: str):
    """Кастомный эндпоинт удаления пользователей. Запрет метода delete.
    Рекомендуется деактивировать пользователей.
    Путь и тег роутера полностью копируют параметры эндпоинта по умолчанию."""
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail="Удаление пользователей запрещено!",
    )
