from app.exceptions import (
    InvalidFileFormatError,
    IncorrectFileColumnsError,
    IncorrectGradeRangeError,
    IncorrectGradeTypeError,
    IncorrectStudentColumnError,
    EmptyCsvFileError,
    MissingValuesError,
    DatabaseOperationError,
)

def test_invalid_file_format_error():
    error = InvalidFileFormatError()
    assert error.message == "only .csv files are allowed"
    assert error.field_name == "file"
    assert error.error_code == "invalid_file_format"


def test_incorrect_file_columns_error():
    error = IncorrectFileColumnsError(["grade", "student"])
    assert error.message == "missing required columns: ['grade', 'student']"
    assert error.field_name == "columns"
    assert error.error_code == "incorrect_file_columns"
    assert error.missing_columns == ["grade", "student"]


def test_incorrect_grade_range_error():
    error = IncorrectGradeRangeError()
    assert error.message == "grade must be between 0 and 5"
    assert error.field_name == "grade"
    assert error.error_code == "incorrect_grade_range"


def test_incorrect_grade_type_error():
    error = IncorrectGradeTypeError()
    assert error.message == "grade must be an integer"
    assert error.field_name == "grade"
    assert error.error_code == "incorrect_grade_type"


def test_incorrect_student_column_error():
    error = IncorrectStudentColumnError()
    assert error.message == "student column contains invalid values"
    assert error.field_name == "student"
    assert error.error_code == "incorrect_student_column"


def test_empty_csv_file_error():
    error = EmptyCsvFileError()
    assert error.message == "csv file is empty"
    assert error.field_name == "file"
    assert error.error_code == "empty_csv_file"


def test_missing_values_error():
    error = MissingValuesError()
    assert error.message == "there are some missing values in file"
    assert error.field_name == "values"
    assert error.error_code == "missing_values_error"


def test_database_operation_error():
    error = DatabaseOperationError()
    assert error.message == "database operation failed"
    assert error.field_name == "database"
    assert error.error_code == "database_operation_error"