def get_all_projects(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_projects")
    return cursor.fetchall()
def find_projects_by_status(connection, status):
    cursor = connection.cursor()
    cursor.execute(
    "SELECT * FROM student_projects WHERE status = ?",
    (status,)
    )
    return cursor.fetchall()
def get_top_projects(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute(
    """
    SELECT student_name, project_topic, status, score
    FROM student_projects
    ORDER BY score DESC
    LIMIT ?
    """,
    (limit,)
    )
    return cursor.fetchall()
