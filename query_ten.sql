SELECT DISTINCT subjects.subject
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.id = teachers.subject_id
WHERE students.student = 'Lawrence Carter' AND teachers.teacher = 'Veronica Clark';
