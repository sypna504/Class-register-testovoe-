from app.db.connections import Connection
from app.exceptions import DatabaseOperationError

class GradesRepository:
    """класс для работы с бд"""

    def get_students_by_twos_count(self, more_than=None | int, les_than=None | int) -> list[tuple[str, int]]:
        """метод подключается к бд
        в зависимости от значения параметра more_than или les_than находит людей с определенным колличеством 2
        при more_than: находит студентов у которых 2 больше чем значение more_than(3)
        при les_than: находит студентов у которых 2 меньше чем значение les_than(5)
        возвращает список этих студентов с количеством 2"""
        try:
            conn = Connection().get_conn()
            cur = conn.cursor()
            if more_than is not None:
                cur.execute(
                    "SELECT student, COUNT(*) AS grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)>%s",
                    (more_than,)
                )
            if les_than is not None:
                cur.execute(
                    "SELECT student, COUNT(*) AS grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)<%s",
                    (les_than,)
                )
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return rows
        except DatabaseOperationError as ex:
            raise DatabaseOperationError(f"ошибка базы даннызх {ex}")
    
    def delete_prev_table(self) -> None:
        """функция для сбрасывания прошлой таблицы
        удаляет прошлую таблицу"""
        conn = Connection().get_conn()
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE grades")
        conn.commit()
        cur.close()


    def insert_into_table(self, rows) -> None:
        """метод для вставления данных в таблицу
        подключается к бд
        сбразывает прошлую таблицу
        заполняет таблицу новыми значениями из .csv файла"""
        conn = Connection().get_conn()
        cur = conn.cursor()
        self.delete_prev_table()
        for row in rows:
                cur.execute(
                    "INSERT INTO grades (student, grade) VALUES (%s, %s)",
                    row,
                )
            
        conn.commit()
        cur.close()
