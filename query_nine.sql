SELECT subjects.subject
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.student = 'John Rush'
GROUP BY subjects.subject;
