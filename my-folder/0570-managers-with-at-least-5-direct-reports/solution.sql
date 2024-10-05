# Write your MySQL query statement below
Select e.name
From Employee e
Join Employee b on e.id=b.managerID 
GROUP BY b.managerId 
HAVING COUNT(*) >= 5

