
import os
import pytest
from flask import g, session
from main import APP


@pytest.fixture
def client():
    APP.config['TESTING'] = True

    with APP.test_client() as client:
        yield client

def login(client, username):
    return client.post('/login', data=dict(
        username=username
    ), follow_redirects=True)
