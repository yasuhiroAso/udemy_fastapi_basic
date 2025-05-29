from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class ContactBase(BaseModel):  # Pydantic継承することでスキーマ定義が可能
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)

    class Config:
        from_attributes = True


class ContactDetail(ContactBase):  # ContactBaseの設定情報をまるっと継承
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ContactCreate(ContactBase):
    pass


class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    created_at: datetime

    class Config:
        from_attributes = True
