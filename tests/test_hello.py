import string


from useful.functions import hello

def test_hello():
    return type(hello("Matt")) == string
