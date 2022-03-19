import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_FirstCreditCard():
    print("Good Morning")    


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
