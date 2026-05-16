from fastapi.testclient import TestClient
from app.main import app
from constraints import VALID_TESTING_FILE
from testss.tests_upload import upload_file
from app.db.grades_repository import GradesRepository

client = TestClient(app)


def test_endp_more_than_3(file_name = VALID_TESTING_FILE):
    response = upload_file(file_name)
    assert response.status_code == 200
    resp = client.get("/students/more-than-3-twos")
    assert resp.status_code == 200
    res = resp.json()
    print(res)
    for student in res:
        print(student)
        assert (student["count_twos"] >= 3)

def test_not_empty_res_less_than_5(file_name = VALID_TESTING_FILE):
    response = upload_file(file_name)
    assert response.status_code == 200
    resp = client.get("/students/less-than-5-twos")
    res = resp.json()
    for student in res:
        full_name = student.get("full_name", None)
        count = student.get("count_twos", None)
        assert full_name is not None
        assert count is not None

def test_not_empty_res_more_than_3(file_name = VALID_TESTING_FILE):
    response = upload_file(file_name)
    assert response.status_code == 200
    resp = client.get("/students/more-than-3-twos")
    res = resp.json()
    for student in res:
        full_name = student.get("full_name", "-")
        count = student.get("count_twos", "-")
        assert full_name != "-"
        assert count != "-"
    
def test_endp_less_than_5(file_name = VALID_TESTING_FILE):
    response = upload_file(file_name)
    assert response.status_code == 200
    resp = client.get("/students/less-than-5-twos")
    assert resp.status_code == 200
    res = resp.json()
    for student in res:
        print(student)
        assert (student["count_twos"] <=5)
    

def test_duble_uppload(file_name = VALID_TESTING_FILE):
    print("test duble uppload")
    response_1 = upload_file(file_name)
    assert response_1.status_code == 200
    resp_1 = client.get("/students/less-than-5-twos")
    assert resp_1.status_code == 200
    res_1 = resp_1.json()
    
    response_2 = upload_file(file_name)
    assert response_2.status_code == 200
    resp_2 = client.get("/students/less-than-5-twos")
    assert resp_2.status_code == 200
    res_2 = resp_2.json()
    print("upload 1")
    print(res_1)
    print("upload 2")
    print(res_2)
    assert res_1 == res_2

def test_on_empty_or_unuploaded_file_less_than_5_and_more_than_3(file_name = VALID_TESTING_FILE):
    GradesRepository().delete_prev_table()
    response = client.get("/students/less-than-5-twos")
    assert response.status_code == 200
    res = response.json()
    print(res)
    for student in res:
        assert student["full_name"]==[]
        assert student["count_twos"]==[]



    