from fastapi import APIRouter

router = APIRouter()


@router.get("/contacts")
async def get_contact_all():
    pass


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
