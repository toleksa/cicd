import os

def test_index():
    os.path.exists("www/index.html")
    assert os.path.getsize("index.html") == 200

