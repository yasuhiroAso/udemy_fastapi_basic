from fastapi import APIRouter
import schemas.contact as cs
from datetime import datetime

router = APIRouter()


@router.get("/contacts", response_model=list[cs.Contact])
async def get_contact_all():
    dummy_date = datetime.now()
    return [
        cs.Contact(
            id=1,
            name="yamada",
            email="test@test.com",
            url="https://test.com",
            gender=1,
            message="テスト",
            is_enabled=False,
            created_at=dummy_date,
        )
    ]


@router.post("/contacts")
async def create_contact():
    pass


@router.get("/contacts/{id}")
async def get_contact():
    pass


@router.put("/contacts/{id}")
async def update_contact():
    pass


@router.delete("/contacts/{id}")
async def delete_contact():
    pass
