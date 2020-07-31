import pytest
import requests


@pytest.mark.parametrize("code", [404])
def test_url_status(url, code, method):
    response = method(url + "/status/{}".format(code))
    assert response.status_code == code