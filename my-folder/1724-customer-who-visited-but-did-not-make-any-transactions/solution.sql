# Write your MySQL query statement below
Select v.customer_id, count(v.visit_id) as count_no_trans
From Visits v left join Transactions t on v.visit_id=t.visit_id
Where t.transaction_id is null Group By v.customer_id;

