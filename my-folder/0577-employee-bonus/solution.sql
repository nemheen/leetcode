# Write your MySQL query statement below
Select e.name, b.bonus
From Employee e
Left Join Bonus b 
On e.empID=b.empID 
WHere b.bonus < 1000 or b.bonus is null
