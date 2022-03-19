import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created.")
    return ["Nicolas", "Brown", "nicolasbrown.com"]

@pytest.fixture(params=[("chrome", "Nicolas", "Brown"), ("Firefox", "Nico"), ("IE", "SS")])    
def crossBrowser(request):
    return request.param