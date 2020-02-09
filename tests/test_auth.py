import pytest
from flask import g, session

def test_login(client, auth):
    
    assert client.get('/signin').status_code == 200

    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'
