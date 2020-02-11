from main import APP, socketio

def test_socketio():

    APP.config['WTF_CSRF_ENABLED'] = False

    flask_test_client = APP.test_client()

    socketio_test_client = socketio.test_client(
        APP, flask_test_client=flask_test_client)

    assert socketio_test_client.is_connected()

    r = flask_test_client.post('/', data={
        'email': 'hancoir@gmail.com', 'password': '123456'})
    assert r.status_code == 307

    socketio_test_client = socketio.test_client(
        APP, flask_test_client=flask_test_client)

    socketio_test_client.send({'room': 'room1', 'data': 'This is a test'})
    r = socketio_test_client.get_received()

    assert len(r) == 1
    message = r[0].get('args').get('data')
    assert message == 'This is a test'