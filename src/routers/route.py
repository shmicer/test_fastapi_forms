from fastapi import APIRouter, Body

from services.services import find_and_validate_template

router = APIRouter()


@router.get('/')
async def mainpage() -> str:
    return 'YOU ARE ON THE MAIN PAGE'


@router.post('/get_form')
async def get_form(data: dict = Body(...)):
    return find_and_validate_template(data)
