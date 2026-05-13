from app.exceptions import IncorrectFileColumnsError, IncorrectStudentColumnError, IncorrectGradeRangeError
from app.exceptions import EmptyCsvFileError, MissingValuesError,IncorrectGradeTypeError


class Validator:
    def validate_cols(self, df):
        if "student" not in df.columns or "grade" not in df.columns:
            raise IncorrectFileColumnsError(list({"student", "grade"}))
        
        if df["student"].str.strip().eq("").any():
            raise IncorrectStudentColumnError()
        
    def validate_grade_type(self, df):
        try:
            df["grade"] = df["grade"].astype("int")
        except IncorrectGradeTypeError as e:
            raise e

    def validate_student_type(self, df):
        try:
            df["student"] = df["student"].astype("str")
        except Exception as e:
            raise e
        
    def normalize_studetn(self,df):
        df["student"] = df["student"].str.strip().lower()

    def validate_not_empty(self, df):
        if len(df)==0:
            raise EmptyCsvFileError("файл пустой")
    
    def validate_no_missing_values(self, df):
        if df[["student", "grade"]].isna().any().any():
            raise MissingValuesError("некоторые значения пропущенны, файл некоректен")
        df = df.dropna()
    
    def validate_grade_range(self, df):
        if (((df["grade"]<0) | (df["grade"]>5))).any():
            raise IncorrectGradeRangeError("оценки должа быть между больше 0 и меньше 5")
    
    def validate(self, df):
        self.validate_not_empty(df)
        self.validate_student_type(df)
        self.validate_cols(df)
        self.validate_grade_type(df)
        self.validate_no_missing_values(df)
        self.validate_grade_type(df)
        self.validate_grade_range(df)


            
    