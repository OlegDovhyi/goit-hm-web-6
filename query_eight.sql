SELECT AVG(grades.total) as average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN teachers ON students.group_id = teachers.subject_id
WHERE teachers.teacher = 'Michael Hernandez';
