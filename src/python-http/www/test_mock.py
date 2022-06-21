from http.server import HTTPServer
import pytest
import requests

@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8888)

def http_check(httpserver, endpoint="/", code=200):
    httpserver.expect_request(endpoint).respond_with_data()
    response = requests.get(httpserver.url_for(endpoint))
    assert response.status_code == code

def test_json_client(httpserver):
    httpserver.expect_request("/foobar").respond_with_json({"foo": "bar"})
    assert requests.get(httpserver.url_for("/foobar")).json() == {'foo': 'bar'}

def test_a(httpserver):
    http_check(httpserver)
    http_check(httpserver,"/logo.png",200)
    #http_check(httpserver,"/foobar",404)

def test_root(httpserver: HTTPServer):
    endpoint = "/"
    httpserver.expect_request(endpoint).respond_with_data()
    response = requests.get(httpserver.url_for(endpoint))
    print(response)
    assert response.status_code == 200

def test_logo(httpserver: HTTPServer):
    endpoint = "/logo.png"
    httpserver.expect_request(endpoint).respond_with_data()
    response = requests.get(httpserver.url_for(endpoint))
    print(response)
    assert response.status_code == 200

def test_foobar_404(httpserver: HTTPServer):
    endpoint = "/foobar"
    httpserver.expect_request(endpoint).respond_with_data("dupa8")
    #response = requests.get(httpserver.url_for(endpoint))
    response = requests.get("http://localhost:8888/foobar")
    #assert response.status_code == 404
    #assert dir(response) == "qwe"
    assert response.content.decode() == "dupa8"

