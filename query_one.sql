SELECT students.student, AVG(grades.total) as average_score
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.student
ORDER BY average_score DESC
LIMIT 5;
