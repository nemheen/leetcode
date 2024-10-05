# Write your MySQL query statement below
Select s.student_id, s.student_name, sub.subject_name, count(e.student_id) as attended_exams
From Students s
Cross Join Subjects sub
Left Join Examinations e
ON sub.subject_name=e.subject_name and s.student_id=e.student_id
Group BY sub.subject_name, s.student_name
Order By s.student_id, sub.subject_name

