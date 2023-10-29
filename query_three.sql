SELECT groups.id, groups.group_number, AVG(grades.total) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 2
GROUP BY groups.id, groups.group_number;
