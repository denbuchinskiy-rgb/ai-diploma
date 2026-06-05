def clear_projects(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM student_projects")
    connection.commit()
def add_project(connection, student_name, project_topic, status, score, comment):

    cursor = connection.cursor()
    cursor.execute(
    """
    INSERT INTO student_projects (
    student_name,
    project_topic,
    status,
    score,
    comment
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (student_name, project_topic, status, score, comment)
    )
    connection.commit()
def seed_demo_projects(connection):
    clear_projects(connection)
    add_project(connection, "Алексей Смирнов", "Разработка веб-сервиса для бронирования", "Зачтено", 92, "Проект выполнен в срок. Архитектура хорошо продумана.")
    add_project(connection, "Мария Петрова", "Нейросеть для классификации текстов", "На проверке", 0, "Проект на стадий выполнения")
    add_project(connection, "Дмитрий Васильев", "Мобильное приложение «Фитнес-трекер»", "Не зачтено", 48, "Недостаточно реализован функционал. Требуется доработка бэкенда.")
    add_project(connection, "Екатерина Соколова", "Анализ данных о продажах в ритейле", "Зачтено", 88, "Отличная визуализация данных и выводы. Небольшие замечания по коду.")
    add_project(connection, "Андрей Лебедев", "Система управления задачами (Task Manager)", "На доработке", 60, "Базовый функционал работает, но интерфейс требует существенного улучшения.")

