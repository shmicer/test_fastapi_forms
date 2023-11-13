import re
from datetime import datetime

from config.database import template_collection

ALLOWED_STRING_FORMATS = ['%d.%m.%Y', '%Y-%m-%d']


def list_templates(templates):
    res = []
    for document in templates:
        document['_id'] = str(document['_id'])
        res.append(document)
    return res


def validate_type(value):
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


def find_template(data):
    records = template_collection.find({})
    for template in records:
        template_fields = set(template.keys()) - {'name'} - {'_id'}
        data_fields = set(data.keys())
        if template_fields.issubset(data_fields):
            matching = all(
                data[field] and template[field] == validate_type(data[field])
                for field in data_fields
            )
            if matching:
                return template['name']
    return None
