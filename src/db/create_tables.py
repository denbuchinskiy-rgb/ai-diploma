def create_projects_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    project_topic TEXT,
    status TEXT,
    score REAL,
    comment TEXT
    )
    """
    )
    connection.commit()
