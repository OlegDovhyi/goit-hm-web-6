from datetime import datetime
from faker import Faker
import random
import sqlite3

fake = Faker()

def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('home.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('home.db') as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)

create_db()

conn = sqlite3.connect('home.db')
cursor = conn.cursor()

# Заповнення таблиці груп
for _ in range(3):
    group_number = fake.unique.random_int(min=1, max=999)
    cursor.execute("INSERT INTO groups (group_number) VALUES (?)", (group_number,))
    group_id = cursor.lastrowid
    # Заповнення таблиці студентів
    for _ in range(random.randint(10, 20)):
        student_name = fake.name()
        cursor.execute("INSERT INTO students (student, group_id) VALUES (?, ?)", (student_name, group_id))
        student_id = cursor.lastrowid
        number_of_subjects = random.randint(5, 8)
        for _ in range(random.randint(1, 20)):
            date_of = fake.date_between(start_date='-5y', end_date='today')
            total = random.randint(60, 100)            
            subject_id = random.randint(1, number_of_subjects)
            cursor.execute("INSERT INTO grades (student_id, subject_id, date_of, total) VALUES (?, ?, ?, ?)", (student_id, subject_id, date_of, total))

# Заповнення таблиці вчителів та предметів
subjects = ['Математика', 'Фізика', 'Хімія', 'Інформатика', 'Англійська', 'Історія', 'Біологія', 'Географія']
number_of_subjects = random.randint(5, 8)  
fake_teachers_names = [fake.name() for _ in range(random.randint(3, 5))] 

for name in fake_teachers_names:
    cursor.execute("INSERT INTO teachers (teacher) VALUES (?)", (name,))
    teacher_id = cursor.lastrowid

    selected_subjects = random.sample(subjects, number_of_subjects)
    
    for subject in selected_subjects:
        cursor.execute("SELECT id FROM subjects WHERE subject = ?", (subject,))
        existing_subject = cursor.fetchone()
        
        if existing_subject:
            subject_id = existing_subject[0]
        else:
            cursor.execute("INSERT INTO subjects (subject) VALUES (?)", (subject,))
            subject_id = cursor.lastrowid
        
        cursor.execute("UPDATE teachers SET subject_id = ? WHERE id = ?", (subject_id, teacher_id))

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання
conn.close()
