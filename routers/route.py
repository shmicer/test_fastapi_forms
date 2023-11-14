from fastapi import APIRouter, Body

from config.database import template_collection
from schema.schemas import find_template, list_templates, validate_type

router = APIRouter()


@router.get('/')
async def mainpage() -> str:
    return 'YOU ARE ON THE MAIN PAGE'


@router.get('/get_records')
async def get_records() -> list:
    records = list_templates(template_collection.find())
    return records


@router.post('/get_form')
async def get_form(data: dict = Body(...)):
    template_name = find_template(data)
    if template_name:
        return template_name
    else:
        field_types = {field: validate_type(data[field]) for field in data}
        return field_types
