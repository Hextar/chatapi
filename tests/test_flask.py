
import os
import pytest
from flask import g, session
from main import APP


@pytest.fixture
def client():
    APP.config['TESTING'] = True
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with APP.test_client() as client:
        yield client

def test_login(client):
    return client.post('/', data=dict(
        email='hancoir@gmail.com',
        password='123456'
    ), follow_redirects=True)
