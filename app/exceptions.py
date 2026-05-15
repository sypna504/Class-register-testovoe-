class AppError(Exception):
    """базовая ошибка приложения
    от неё наследуются все остальные пользовательские ошибки"""

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        error_code: str | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.field_name = field_name
        self.error_code = error_code


class InvalidFileFormatError(AppError):
    """ошибка неправильного формата файла
    например пользователь загрузил не .csv файл"""

    def __init__(self, message: str = "only .csv files are allowed"):
        super().__init__(
            message=message,
            field_name="file",
            error_code="invalid_file_format",
        )


class IncorrectFileColumnsError(AppError):
    """ошибка неправильных колонок в CSV
    например, нет колонок student или grade"""

    def __init__(self, missing_columns: list[str]):
        message = f"missing required columns: {missing_columns}"

        super().__init__(
            message=message,
            field_name="columns",
            error_code="incorrect_file_columns",
        )

        self.missing_columns = missing_columns


class IncorrectStudentColumnError(AppError):
    """ошибка в колонке student
    например, имя студента пустое"""

    def __init__(self, message: str = "student column contains invalid values"):
        super().__init__(
            message=message,
            field_name="student",
            error_code="incorrect_student_column",
        )


class IncorrectGradeRangeError(AppError):
    """ошибка диапазона оценок
    например, grade меньше 0 или больше 5"""

    def __init__(self, message: str = "grade must be between 0 and 5"):
        super().__init__(
            message=message,
            field_name="grade",
            error_code="incorrect_grade_range",
        )


class IncorrectGradeTypeError(AppError):
    """ошибка типа оценки
    например, в grade лежит текст вместо числа"""

    def __init__(self, message: str = "grade must be an integer"):
        super().__init__(
            message=message,
            field_name="grade",
            error_code="incorrect_grade_type",
        )

class EmptyCsvFileError(AppError):
    """ошибка пустого CSV-файла"""

    def __init__(self, message: str = "csv file is empty"):
        super().__init__(
            message=message,
            field_name="file",
            error_code="empty_csv_file",
        )


class DatabaseOperationError(AppError):
    """ошибка при работе с базой данных"""

    def __init__(self, message: str = "database operation failed"):
        super().__init__(
            message=message,
            field_name="database",
            error_code="database_operation_error",
        )
    
class MissingValuesError(AppError):
    """ошибка пропущенны значенийнапример, в grade или в student есть какие то пропущенные значения"""

    def __init__(self, message: str = "missing values"):
        super().__init__(
            message=message,
            field_name="values",
            error_code="missing_values_error",
        )