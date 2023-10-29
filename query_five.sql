SELECT subjects.subject
FROM subjects
JOIN teachers ON subjects.id = teachers.subject_id
WHERE teachers.teacher = 'Veronica Clark';
