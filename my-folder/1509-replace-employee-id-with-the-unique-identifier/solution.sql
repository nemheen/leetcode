# Write your MySQL query statement below
Select eu.unique_id as unique_id, e.name as name
From Employees e left join EmployeeUNI eu on e.id=eu.id

