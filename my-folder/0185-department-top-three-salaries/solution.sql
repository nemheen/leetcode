# Write your MySQL query statement below
Select e.name as Employee, d.name as Department, e.salary as Salary
From (select name, departmentID, salary, dense_rank() over (partition by departmentId order by salary desc) as rk from Employee) e left join Department d on e.departmentId=d.id
where rk<=3;


