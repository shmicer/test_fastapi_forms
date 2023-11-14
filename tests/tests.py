import random

import pytest
from fastapi.testclient import TestClient

from main import app

test_data = [
    {
        "name": "Subscription form",
        "data": {
            "user_phone": "+ 8 988 000 00 00",
            "date": "01.01.2023"
        }
    },
    {
        "name": "SMS text form",
        "data": {
            "phone_number": "+ 7 900 222 22 22",
            "text": "text"
        }
    },
    {
        "name": "Birthday form",
        "data": {
            "birthday_date": "2023-02-03",
            "congratulation": "text"
        }
    },
    {
        "name": "Order form",
        "data": {
            "customer_email": "abc@abc.com",
            "customer_phone": "+7 900 000 00 00",
            "order_date": "21.01.2012"
        }
    },
    {
        "name": "Subscription form",
        "data": {
            "email": "abc@abc.com",
            "user_phone": "+7 911 456 45 45",
            "text_field": "text"
        }
    },
]


@pytest.fixture
def client():
    return TestClient(app)


def test_get_form_with_matching_template(client):
    data = random.choice(test_data)
    response = client.post('/get_form', json=data['data'])
    assert response.status_code == 200
    assert response.json() == data['name']


def test_get_form_without_matching_template(client):
    data = {
        "customer_email": "abc",
        "customer_phone": "+7 911 000 00 00",
        "order_date": "abc"
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200
    assert response.json() == {
        'customer_email': 'text',
        'customer_phone': 'phone',
        'order_date': 'text'
    }


def test_get_form_with_empty_data(client):
    response = client.post('/get_form')
    assert response.status_code == 422  # Unprocessable Entity
