import os

def test_index():
    os.path.exists("www/index.html")
    assert os.path.getsize("www/index.html") == 200

