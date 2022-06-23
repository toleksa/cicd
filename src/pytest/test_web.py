import requests

def test_server_is_alive():
    response = requests.get("http://webserver:8888/")
    assert response.status_code == 200

def test_server_logo():
    response = requests.get("http://webserver:8888/logo.png")
    assert response.status_code == 200

def test_server_404():
    response = requests.get("http://webserver:8888/foobar")
    assert response.status_code == 404

