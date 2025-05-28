from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class Contact(BaseModel):  # Pydantic継承することでスキーマ定義が可能
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    created_at: datetime
