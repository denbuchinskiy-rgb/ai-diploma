def get_average_score(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(score) FROM student_projects")
    return cursor.fetchone()[0]
def get_status_report(connection):
    cursor = connection.cursor()
    cursor.execute(
    """
    SELECT status, COUNT(*)
    FROM student_projects
    GROUP BY status
    ORDER BY COUNT(*) DESC
    """
    )
    return cursor.fetchall()
