import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_FixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")


    def test_FixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_FixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")

    def test_FixtureDemo4(self):
        print("I will execute steps in fixtureDemo method")

    def test_FixtureDemo5(self):
        print("I will execute steps in fixtureDemo method")


