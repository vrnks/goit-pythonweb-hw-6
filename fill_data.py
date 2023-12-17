import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_PROFESSORS = 5
MAX_GRADES_PER_STUDENT = 20

def generate_fake_data(number_students, number_groups, number_subjects, number_professors, max_grades_per_student) -> tuple:
    fake_data = faker.Faker()

    # групи
    groups = [{'group_id': i + 1, 'group_name': fake_data.word()} for i in range(number_groups)]

    # студенти
    students = [{'student_id': i + 1, 'name': fake_data.name(), 'group_id': choice(groups)['group_id']} for i in range(number_students)]

    #  викладачі
    professors = [{'professor_id': i + 1, 'name': fake_data.name()} for i in range(number_professors)]

    # предмети з вказівкою на викладача
    subjects = [{'subject_id': i + 1, 'subject_name': fake_data.word(), 'professor_id': choice(professors)['professor_id']} for i in range(number_subjects)]

    # оцінки для студентів з предметів
    grades = [{'grade_id': i + 1, 'student_id': choice(students)['student_id'],
               'subject_id': choice(subjects)['subject_id'], 'grade': randint(60, 100) / 10,
               'date_received': fake_data.date_this_decade()} for i in range(max_grades_per_student * number_students)]

    return groups, students, professors, subjects, grades

def main():
    # Підключення до бази даних
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    # Виклик функції та отримання згенерованих даних
    groups, students, professors, subjects, grades = generate_fake_data(
        NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_PROFESSORS, MAX_GRADES_PER_STUDENT
    )

    # Заповнення таблиць даними
    cursor.execute("DELETE FROM Groups;") 
    cursor.executemany("INSERT INTO Groups (group_id, group_name) VALUES (?, ?)", [(group['group_id'], group['group_name']) for group in groups])
    cursor.execute("DELETE FROM Students;") 
    cursor.executemany("INSERT INTO Students (student_id, name, group_id) VALUES (?, ?, ?)", [(student['student_id'], student['name'], student['group_id']) for student in students])
    cursor.execute("DELETE FROM Professors;")
    cursor.executemany("INSERT INTO Professors (professor_id, name) VALUES (?, ?)", [(professor['professor_id'], professor['name']) for professor in professors])
    cursor.execute("DELETE FROM Subjects;")
    cursor.executemany("INSERT INTO Subjects (subject_id, subject_name, professor_id) VALUES (?, ?, ?)", [(subject['subject_id'], subject['subject_name'], subject['professor_id']) for subject in subjects])
    cursor.execute("DELETE FROM Grades;")
    cursor.executemany("INSERT INTO Grades (grade_id, student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?, ?)", [(grade['grade_id'], grade['student_id'], grade['subject_id'], grade['grade'], grade['date_received']) for grade in grades])

    # Зберігання змін та закриття з'єднання
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
