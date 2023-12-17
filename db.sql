DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);

DROP TABLE IF EXISTS Groups;
CREATE TABLE Groups (
    group_id INT PRIMARY KEY,
    group_name VARCHAR(255)
);

DROP TABLE IF EXISTS Professors;
CREATE TABLE Professors (
    professor_id INT PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS Subjects;
CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(255),
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
);

DROP TABLE IF EXISTS Grades;
CREATE TABLE Grades (
    grade_id INT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade FLOAT,
    date_received DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);
