from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import models.contact as contact_model


async def create_contact(
    db: AsyncSession, contact: contact_schema.ContactCreate
) -> contact_model.Contact:
    """
    DBに保存
    引数：
        db: DBセッション
        contact: 作成するコンタクトのデータ
    戻り値:
        作成されたORMモデル
    """
    contact_data = contact.model_dump()
    if contact_data["url"] is not None:
        contact_data["url"] = str(contact_data["url"])

    db_contact = contact_model.Contact(
        **contact_data
    )  # db保存はsqlalchemyのモデル、インスタンス化

    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact
