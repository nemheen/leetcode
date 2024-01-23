SELECT E.name AS Employee
FROM Employee E
Join Employee M on E.managerId=M.id
WHERE E.salary > M.salary and E.managerId is not null;

