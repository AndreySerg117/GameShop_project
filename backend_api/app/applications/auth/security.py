from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from applications.users.crud import get_user_by_email
from applications.users.models import User
from sqlalchemy.ext.asyncio import AsyncSession

from database.session_dependencies import get_async_session


class SecurityHandler:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(
    token: str = Depends(SecurityHandler.oauth2_scheme),
    session: AsyncSession = Depends(get_async_session),
) -> User:

    # user = await get_user_by_email(user_email, session)
    pass