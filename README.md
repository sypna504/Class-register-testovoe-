## как запустить
 - перейти в корень проекта
 - переименновать файл .env.example в .env
 - создать папку с названием ```data``` в корне 
 - собрать докер композ ```docker compose up --build ```
 - перейти по адресу http://localhost:8000/docs

## формат csv
файл должен быть `.csv` и содержать колонки для корректной работы

```csv
student,grade
ivan,2
anna,5
```

## endpoints
 - POST /upload-grades - загрузить файл
 - GET /students/more-than-3-twos - получить студентов у которых больше 3 двоек
 - GET /students/less-than-5-twos - получить студентов у которых меньше 5 двоек

## как запустить тесты
 - скачать зависимости ``` python -m pip install -r requirements.txt```
 - установить pytest python ```-m pip install pytest httpx```
 - поднять бд ```docker compose up``` 
 - запустить тесты python ```-m pytest tests/tests_upload.py -v```

## status codes ошибок
- `400` - неправильный файл
- `422` - неправильные данные внутри csv
- `500` - ошибка сервера или базы данных

## архитектура 

```text
Class-register-testovoe-/
├── app/
│   ├── main.py
│   ├── exceptions.py
│   ├── db/
│   │   ├── connections.py
│   │   └── grades_repository.py
│   ├── parsers/
│   │   └── csv_parser.py
│   ├── routers/
│   │   └── grades_router.py
│   ├── schemas/
│   │   └── grades_schema.py
│   ├── grades_service.py
│   └── grades_validator.py
├── files_for_tests/
│   ├── valid_grades.csv
│   ├── missing_columns.csv
│   ├── invalid_grade_range.csv
│   ├── invalid_grade_type.csv
│   ├── missing_values.csv
│   ├── empty_grades.csv
│   └── test_file.cvs
├── tests/
│   └── tests_upload.py
├── data
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── constraints.py
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── requirements.txt
└── README.md