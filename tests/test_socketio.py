from main import APP, socketio

def socketio_test():

    flask_test_client = app.test_client()

    socketio_test_client = socketio.test_client(
        app, flask_test_client=flask_test_client)

    assert not socketio_test_client.is_connected()

    r = flask_test_client.post('/login', data={
        'username': 'handerson.contreras@gmail.com', 'password': '123456'})
    assert r.status_code == 200

    socketio_test_client = socketio.test_client(
        app, flask_test_client=flask_test_client)

    r = socketio_test_client.get_received()

    assert len(r) == 1
    assert r[0]['name'] == 'welcome'
    assert len(r[0]['args']) == 1
    assert r[0]['args'][0] == {'username': 'python'}