from http.client import responses
import pytest
import requests

base_url = "https://yougile.com"
Key = ""

# Функция к методу GET получить


def get_project_list():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + Key
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    return resp.json()

# Функция к методу POST создать


def create_project(title):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + Key
    }
    project = {"title": title}
    resp = requests.post(base_url + '/api-v2/projects',
                         headers=headers, json=project)
    return resp.json()

# Функции к методу GET получить по ID


def get_project_id(project_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + Key
    }
    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.get(url, headers=headers)
    return resp

# Функции к методу PUT изменить


def change_project(project_id, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + Key
    }
    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.put(url, headers=headers, json=data)
    return resp

# Позитивные и негативные тесты на метод POST


def test_create_project_positive():
    body = get_project_list()
    len_before = body["paging"]["count"]

    title = "AUDY"
    result = create_project(title)
    print(result)
    new_id = result["id"]

    body = get_project_list()
    len_after = body["paging"]["count"]

    # assert .status_code == 201
    assert len_after - len_before == 1
    assert body['content'][-1]["id"] == new_id


def test_create_project_negative():
    body = get_project_list()
    len_before = body["paging"]["count"]

    title = ''
    create_project(title)

    body = get_project_list()
    len_after = body["paging"]["count"]

    assert len_after - len_before == 0

# Позитивные и негативные тесты на метод GET получить по ID


def test_get_project_id_positive():
    my_project_id = "d6c7a00d-065f-48c9-aeb8-0a0d9910110d"
    response = get_project_id(my_project_id)
    assert response.status_code == 200


def test_get_project_id_negative():
    my_project_id = "123456789"
    response = get_project_id(my_project_id)
    assert response.status_code == 404

# Позитивные и негативные тесты на метод PUT


def test_change_project_positive():
    my_project_id = "d6c7a00d-065f-48c9-aeb8-0a0d9910110d"
    data = {'title': 'MERCEDES'}
    response = change_project(my_project_id, data)
    assert response.status_code == 200


def test_change_project_negative():
    my_project_id = "d6c7a00d-065f-48c9-aeb8-0a0d9910110d"
    data = {'title': ''}
    response = change_project(my_project_id, data)
    assert response.status_code == 400
