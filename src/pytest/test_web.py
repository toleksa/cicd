import requests

def test_server_is_alive():
    response = requests.get("http://webserver/")
    assert response.status_code == 200

def test_server_logo():
    response = requests.get("http://webserver/logo.png")
    assert response.status_code == 200

def test_server_404():
    response = requests.get("http://webserver/foobar")
    assert response.status_code == 404

