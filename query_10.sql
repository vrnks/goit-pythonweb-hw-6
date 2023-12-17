SELECT Subjects.subject_id, subject_name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
WHERE student_id = 10 AND professor_id = 5
GROUP BY Subjects.subject_id;
