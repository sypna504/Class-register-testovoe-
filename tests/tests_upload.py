from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
# from .constraints import TESTING_FILES_DIR
from pathlib import Path
TESTING_FILES_DIR = Path("files_for_tests")


client = TestClient(app)


def upload_file(filename):
    file_path = TESTING_FILES_DIR/filename

    with open(file_path, "rb") as file:
        return client.post(
            "/upload-grades",
            files={"file": (filename, file, "text/csv")},
        )

def test_valid_grades_file():
    response = upload_file("valid_grades.csv")

    print(response.json())

    assert response.status_code == 200
    
def test_missing_columns_file():
    response = upload_file("missing_columns.csv")

    assert response.status_code == 422

def test_invalid_grade_range_file():
    response = upload_file("invalid_grade_range.csv")

    assert response.status_code == 422

def test_invalid_grade_type_file():
    response = upload_file("invalid_grade_type.csv")

    assert response.status_code == 422

def test_missing_values_file():
    response = upload_file("missing_values.csv")

    assert response.status_code == 422

def test_empty_grades_file():
    response = upload_file("empty_grades.csv")

    assert response.status_code in [400, 422]

def test_wrong_extension_file():
    response = upload_file("test_file.cvs")

    assert response.status_code == 422



