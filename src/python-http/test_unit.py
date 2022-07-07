import os

def test_index():
    os.path.exists("www/index.html")
    assert os.path.getsize("www/index.html") == 57

def test_logo():
    os.path.exists("www/logo.png")
    assert os.path.getsize("www/logo.png") == 11543

