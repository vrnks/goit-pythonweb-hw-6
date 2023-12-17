SELECT Subjects.subject_id, subject_name
FROM Grades
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE student_id = 10
GROUP BY Subjects.subject_id;
