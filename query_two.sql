SELECT students.id, students.student, AVG(grades.total) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 2
GROUP BY students.id, students.student
ORDER BY average_grade DESC
LIMIT 1;
