SELECT Groups.group_id, AVG(grade) as avg_grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Groups ON Students.group_id = Groups.group_id
WHERE subject_id = 4
GROUP BY Groups.group_id;
