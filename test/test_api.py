import pytest
from fastapi.testclient import TestClient
from api import app
from models import Users

client = TestClient(app)

@pytest.fixture
def mongo_find_all_user_results():
    return '[{"id":"6789ca209e4696554185719b","phone_number":"00000000000000","ads_enabled":true,"first_name":"alexander","is_active":true,"last_name":"bloodymary","updated_at":"2025-01-17T00:10:19.963000"},{"id":"6789ce4a9e469655418571a6","phone_number":"119237723823","ads_enabled":false,"first_name":"Patrick","is_active":true,"last_name":"Mahomes111111","updated_at":"2025-01-17T00:15:51.369000"},{"id":"6789ceea9e469655418571a9","phone_number":"8548745411","ads_enabled":false,"first_name":"Russell","is_active":true,"last_name":"WIlson","updated_at":"2025-01-17T02:34:52.572000"},{"id":"6789cfd39e469655418571ac","phone_number":"87878787877","ads_enabled":true,"first_name":"Jared","is_active":false,"last_name":"Goff","updated_at":"2025-01-17T02:34:52.572000"},{"id":"6789d1fb9e469655418571b3","phone_number":"58121484745","ads_enabled":true,"first_name":"Hendon","is_active":false,"last_name":"Hooker","updated_at":"2025-01-17T03:54:50.545000"},{"id":"6789d36c9e469655418571b8","phone_number":"1192377238231","ads_enabled":false,"first_name":"Patrick","is_active":true,"last_name":"Mahomes111111","updated_at":"2025-01-17T00:49:47.731000"},{"id":"6789d3a29e469655418571b9","phone_number":"1192371237238231","ads_enabled":false,"first_name":"Patrick","is_active":true,"last_name":"Mahomes111111","updated_at":"2025-01-17T00:50:42.290000"},{"id":"6789d3ac9e469655418571ba","phone_number":"119222371237238231","ads_enabled":false,"first_name":"Patrick","is_active":true,"last_name":"Mahomes111111","updated_at":"2025-01-17T00:51:34.279000"},{"id":"6789d52f9e469655418571c0","phone_number":"494848431121","ads_enabled":false,"first_name":"Michael","is_active":true,"last_name":"Vick","updated_at":"2025-01-17T03:54:50.545000"},{"id":"6789d5d29e469655418571c3","phone_number":"119222371237123123238231","ads_enabled":false,"first_name":"Patrick","is_active":true,"last_name":"Mahomes111111","updated_at":"2025-01-17T01:00:09.279000"},{"id":"6789d61a9e469655418571c5","phone_number":"1618915614","ads_enabled":false,"first_name":"Michael","is_active":true,"last_name":"Jackson","updated_at":"2025-01-17T04:01:18.492000"}]'


@pytest.fixture
def user_dict():
    return [{"id":"6789ca209e4696554185719b","phone_number":"00000000000000","ads_enabled":True,"first_name":"alexander","is_active":True,"last_name":"bloodymary","updated_at":"2025-01-17T00:10:19.963000"}]


@pytest.fixture
def mock_find_all(mocker, mongo_find_all_user_results):
    return mocker.patch(
        'pymongo.collection.Collection.find',
        return_value=mongo_find_all_user_results
    )


def test_get_all_users_should_return_status_code_200():
    # GIVEN
    # WHEN
    response = client.get("/users/")

    # THEN
    assert response.status_code == 200


def test_get_all_users_should_users_list(mongo_find_all_user_results):
    # GIVEN
    # THEN
    results = client.get("/users/")

    assert str(results.text) == mongo_find_all_user_results


def test_get_user_by_phone_number_should_return_status_code_200():
    # GIVEN
    phone_number = '000000000000'

    # WHEN
    response = client.get(f"/users/phone_number/{phone_number}")

    # THEN
    assert response.status_code == 200

def test_get_user_by_object_id_should_return_status_code_200():
    # GIVEN
    object_id = '6789ca209e4696554185719b'

    # WHEN
    response = client.get(f"/users/{object_id}")

    # THEN
    assert response.status_code == 200

