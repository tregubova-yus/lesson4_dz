import pytest
import requests

# 1. Проверка кода доступа на 200
@pytest.mark.parametrize("code", [200])
def test_url_status(url, code, method):
    response = method(url + "/status/{}".format(code))
    assert response.status_code == code


# 2. Проверка, что список с породами не пуст
def test_breeds_list(fixture_dog_url):
    url = fixture_dog_url + f'api/breeds/list/all'
    response = requests.get(url)
    if response.ok:
        get_response = response.json()['message']
    else:
        print('Server not responding')
    if not get_response:
        raise ValueError('Get not load')
    assert len(get_response) != 0


# 3. С параметризацией
# Проверка, что порода bulldog содержит все значения ('bulldog': ['boston', 'english', 'french'])
def test_breeds_list_param(fixture_dog_url, fixture_dict2):
    url = fixture_dog_url + f'api/breeds/list/all'
    response = requests.get(str(url))
    if response.ok:
        get_response = response.json()
    else:
        print('Server not responding')
    if not get_response:
        raise ValueError('Get not load')
    breeds_dict = get_response.get('message')
    new_dict = breeds_dict.get(fixture_dict2)
    assert new_dict == ['boston', 'english', 'french']


# С параметризацией
# 4. Проверка, правильно ли значение заголовка Content Type идентифицирует тело ответа как UTF-8
def test_get_locations_for_us_90210_check_content_type_equals_json(fixture_dog_url,fixture_dict3):
    response = requests.get(fixture_dog_url)
    assert response.headers['Content-Type'] == fixture_dict3


# 5. Проверка получения изображений .jpg
def test_breeds_image_random_one(fixture_dog_url):
    url = fixture_dog_url + f'api/breeds/image/random/'
    response = requests.get(url)
    if response.ok:
        get_response = response.json()
    else:
        print('Server not responding')
    if not get_response:
        raise ValueError('Get not load')
    images = get_response.get('message')
    symbol = ['.jpg']
    coefic = [e for e in symbol if e in images]
    assert coefic == symbol
