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
            name="山田",
            email="test@test.com",
            url="https://test.com",
            gender=1,
            message="テスト",
            is_enabled=False,
            created_at=dummy_date,
        )
    ]


@router.post("/contacts", response_model=cs.Contact)
async def create_contact(body: cs.Contact):
    return cs.Contact(**body.model_dump())


@router.get("/contacts/{id}", response_model=cs.Contact)
async def get_contact(id: int):
    return cs.Contact(id)


@router.put("/contacts/{id}", response_model=cs.Contact)
async def update_contact(id: int, body: cs.Contact):
    return cs.Contact(**body.model_dump)


@router.delete("/contacts/{id}", response_model=cs.Contact)
async def delete_contact(id: int):
    return
