SELECT professor_id, AVG(grade) as avg_grade
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
WHERE professor_id = 4
GROUP BY professor_id;
