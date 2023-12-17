SELECT Students.student_id, name, grade, date_received
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
WHERE group_id = 1 AND subject_id = 1;
