from pydantic import BaseModel, Field

class FileSuccesfullUploaded(BaseModel):
    status: str = Field(description="статус операции")
    records_loaded: int = Field(ge=0, description="количество загруженных записей")
    students: int = Field(ge=0, description="количество уникальных студентов")

class StudentTwosCount(BaseModel):
    full_name: str = Field(description="имя студента")
    count_twos: int = Field(ge=0, description="колличество двоек")

class StudentsTwosResponse(BaseModel):
    students: list[StudentTwosCount]

