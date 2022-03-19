import py
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"


#@pytest.fixture()
#def setup():
#    print("I will be executing first")


def test_FixtureDemo(setup):
    print("I will execute steps in fixtureDemo method 2")




