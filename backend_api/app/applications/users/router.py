from fastapi import APIRouter, status
from applications.users.schemas import UserFields

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
        new_user: UserFields
) -> UserFields:
    return new_user