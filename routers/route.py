from fastapi import APIRouter, Body

from services.services import find_and_validate_template, validate_type, get_all_templates

router = APIRouter()


@router.get('/')
async def mainpage() -> str:
    return 'YOU ARE ON THE MAIN PAGE'


@router.get('/get_records')
async def get_records() -> list:
    records = get_all_templates()
    return records


@router.post('/get_form')
async def get_form(data: dict = Body(...)):
    return find_and_validate_template(data)


