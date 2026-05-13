from app.db.connections import Connection
from app.exceptions import DatabaseOperationError

class GradesRepository:

    def get_students_by_twos_count(self, more_than=None, les_than=None):
        students_with_twos=[]
        try:
            conn = Connection().get_conn()
            cur = conn.cursor()
            if more_than is None:
                cur.execute(
                    "SELECT student, COUNT(*) AS grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)>%s",
                    (more_than,)
                )
            if les_than is None:
                cur.execute(
                    "SELECT student, COUNT(*) AS grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)<%s",
                    (les_than,)
                )
            rows = cur.fetchall()
            for student,cnt in rows:
                students_with_twos.append({
                    "full_name": student,
                    "count_twos": cnt,
                })
            cur.close()
            conn.close()
            return students_with_twos
        except DatabaseOperationError as ex:
            raise DatabaseOperationError(f"ошибка базы даннызх {ex}")

    def insert_into_table(self, rows):
        conn = Connection().get_conn()
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE grades")
        for row in rows:
                cur.execute(
                    "INSERT INTO grades (student, grade) VALUES (%s, %s)",
                    row,
                )
            
        conn.commit()
        cur.close()
