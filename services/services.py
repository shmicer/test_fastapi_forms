import re
from datetime import datetime

from config.database import template_collection

ALLOWED_STRING_FORMATS = ['%d.%m.%Y', '%Y-%m-%d']


def get_all_templates():
    try:
        records = template_collection.find({})
    except Exception as e:
        print(f"Error accessing the database: {e}")
        return None
    return list(records)


all_templates = get_all_templates()


def validate_type(value):
    """
    Функция для валидации типов данных, полученных при запросе
    """
    for fmt in ALLOWED_STRING_FORMATS:
        try:
            _ = datetime.strptime(value, fmt)
            return 'date'
        except ValueError:
            pass
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return 'phone'
    elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        return 'email'
    else:
        return 'text'


def find_and_validate_template(data):
    """
    Функция для валидации полей данных и поиска подходящего шаблона
    """
    data_fields = set(data.keys())

    best_matching_template = None
    best_matching_count = 0

    for template in all_templates:
        template_fields = set(template.keys()) - {'name', '_id'}

        # template and data keys both contain set
        matching = template_fields.intersection(data_fields)
        matching_count = len(matching)

        # check if data's items have valid types with template values
        value_matching = all(template[item] == validate_type(data[item]) for item in matching)

        if matching_count > best_matching_count and value_matching:
            best_matching_template = template['name']
            best_matching_count = matching_count

    field_types = {field: validate_type(data[field]) for field, v in data.items()}

    if best_matching_template:
        return best_matching_template
    else:
        return field_types
