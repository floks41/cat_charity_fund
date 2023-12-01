"""Модуль установки настроек проекта."""


from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """Класс настроке проекта."""
    app_title: str = 'QRKot'
    description: str = (
        'Приложение для Благотворительного фонда поддержки котиков QRKot'
    )
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'EXTREMELY_SECRET_PHRASE'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        """Класс конфигурации настроке проекта, задается имя файла env."""
        env_file = '.env'


settings = Settings()
