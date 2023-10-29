SELECT students.student, grades.total
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
WHERE groups.group_number = 560 AND grades.subject_id = 2;
