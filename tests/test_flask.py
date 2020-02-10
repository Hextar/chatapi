
import os
import pytest
from flask import g, session
from main import APP


@pytest.fixture
def client():
    APP.config['TESTING'] = True

    with APP.test_client() as client:
        yield client

def test_login(client):
    return client.post('/login', data=dict(
        username='handerson.contreras@gmail.com'
    ), follow_redirects=True)
