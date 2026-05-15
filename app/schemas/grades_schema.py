from pydantic import BaseModel, Field

class FileUploadedResponse(BaseModel):
    """схема для ответа после успещной загрузки файла
    status: строка
    rerecords_loaded: число, превышающее 0
    students число, превышающее 0"""

    status: str = Field(description="статус операции")
    records_loaded: int = Field(ge=0, description="количество загруженных записей")
    students: int = Field(ge=0, description="количество уникальных студентов")

class StudentTwosCount(BaseModel):
    """схема для одного студента
    full_name: строка
    count_twos: число, превышающее 0"""

    full_name: str = Field(description="имя студента")
    count_twos: int = Field(ge=0, description="колличество двоек")


