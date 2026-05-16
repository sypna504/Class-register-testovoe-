from app.parsers.csv_parser import CsvParser
from app.db.grades_repository import GradesRepository
from app.exceptions import IncorrectFileColumnsError, IncorrectStudentColumnError, IncorrectGradeRangeError
from app.exceptions import EmptyCsvFileError, MissingValuesError,IncorrectGradeTypeError
import pandas as pd


class Validator:
    """класс для проверки и подготовки данных из .csv перед записью в таблицу"""

    @staticmethod
    def validate_cols(df) -> None:
        """проверяет что в файле есть нужные колонки grade и student
        вызывает IncorrectFileColumnsError если их нет
        вызывает IncorrectStudentColumnError если имя студента пустое"""

        if "student" not in df.columns and "grade" not in df.columns:
            raise IncorrectFileColumnsError(list({"student", "grade"}))
        
        if "grade" not in df.columns:
            raise IncorrectFileColumnsError(list({"grade"}))

        if "student" not in df.columns:
            raise IncorrectFileColumnsError(list({"student"}))
        
        if df["student"].str.strip().eq("").any():
            raise IncorrectStudentColumnError(list({"student"}))
        
    @staticmethod
    def validate_grade_type(df) -> None:
        """проверяет что значения в колонке grade числовые
        вызывает IncorrectGradeTypeError если тип неправильный"""

        try:
            df["grade"] = df["grade"].astype(int)
        except Exception:
            raise IncorrectGradeTypeError()
        
    @staticmethod
    def validate_student_type(df) -> None:
        """проверяет что колонка student строка"""

        try:
            df["student"] = df["student"].astype("str")

        except Exception as e:
            raise e
        
    @staticmethod
    def normalize_student(df) -> None:
        """приводит имена студентов в один формат"""

        df["student"] = df["student"].str.strip().lower()

    @staticmethod
    def validate_not_empty(df) -> None:
        """проверяет что датафрэйм не пустой
        вызывает ошибку EmptyCsvFileError если пустой"""

        if len(df)==0:
            raise EmptyCsvFileError("файл пустой")
    
    @staticmethod
    def validate_missing_values(df) -> None:
        """проверяет нет ли в колонках пропущенных значений
        если есть то вызывает ошибку MissingValuesError файл некоректен """

        if df[["student", "grade"]].isna().any().any():
            raise MissingValuesError("некоторые значения пропущенны, файл некоректен")
    
    @staticmethod
    def validate_grade_range(df) -> None:
        """проверяет что диапозоны значений правильные
        иначе IncorrectGradeRangeError"""

        if (((df["grade"]<0) | (df["grade"]>5))).any():
            raise IncorrectGradeRangeError("оценки должа быть между больше 0 и меньше 5")
    
    def validate(self,df) -> None:
        """запускает все проверки перед сохранением в таблицу"""

        self.validate_not_empty(df)
        self.validate_cols(df)
        self.validate_missing_values(df)
        
        self.validate_grade_type(df)
        self.validate_grade_range(df)
        self.validate_student_type(df)
        self.validate_grade_type(df)

class GradesService:
    """содержит основуню логику работы приложения"""

    def __init__(self, parser, validator, repository):
        """получает парсер, валидатор и репозитори для работы сервиса"""

        self.parser = parser
        self.validator = validator
        self.repository = repository
    
    def grades_from_csv(self, file):
        """читает csv файл
        проверяет данные
        сохраняет в таблицу"""

        df  = self.parser.read(file)
        self.validator.validate(df)
        rows = []
        for _, row in df.iterrows():
            rows.append((row["student"], row["grade"]))
        self.repository.insert_into_table(rows)
        return {
            "status": "ok",
            "records_loaded": len(df),
            "students": df["student"].nunique()
        }
        
    def get_students_with_twos(self, more_than=None, les_than=None):
        """возвращает студентов по колличеству двоек по условию"""

        rows = self.repository.get_students_by_twos_count(more_than=more_than, les_than=les_than,)
        students = []
        for student, count_twos in rows:
            students.append({
                "full_name": student,
                "count_twos": count_twos,
            })

        return students

    

    
        

    