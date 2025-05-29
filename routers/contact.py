from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as cs
import cruds.contact as contact_curd
from database import get_db
from datetime import datetime

router = APIRouter()


@router.get("/contacts", response_model=list[cs.ContactList])
async def get_contact_all(db: AsyncSession = Depends(get_db)):
    return await contact_curd.get_contact_all(db)


@router.post("/contacts", response_model=cs.ContactCreate)
async def create_contact(body: cs.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_curd.create_contact(db, body)


@router.get("/contacts/{id}", response_model=cs.ContactDetail)
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_curd.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/contacts/{id}", response_model=cs.ContactCreate)
async def update_contact(
    id: int, body: cs.ContactCreate, db: AsyncSession = Depends(get_db)
):
    contact = await contact_curd.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_curd.update_contact(db, body, original=contact)


@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_curd.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_curd.delete_contact(db, original=contact)


def get_message():
    message = "hello world"
    print(f"get_messageが実行された：{message}")
    return message


@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"エンドポイントにアクセスがあった：{message}")
    return {"message": message}
