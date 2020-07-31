import pytest
import requests


## Тестовое API: https://www.openbrewerydb.org/


@pytest.fixture()
def fixture_brewery_url():
    return 'https://www.openbrewerydb.org/'

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://www.openbrewerydb.org/",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def method(request):
    m = request.config.getoption("--method")
    if m == "post":
        return requests.post
    elif m == "get":
        return requests.get
    elif m == "delete":
        return requests.delete
    elif m == "put":
        return requests.put
    elif m == "patch":
        return requests.patch

#Для параметризованного теста
@pytest.fixture(params=['United States'])
def fixture_dict2(request):
    return request.param

#Для параметризованного теста
@pytest.fixture(params=['text/html; charset=UTF-8'])
def fixture_dict3(request):
    return request.param

