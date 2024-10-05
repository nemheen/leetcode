# Write your MySQL query statement below
Select p.product_name, s.year, s.price
From Product p left join Sales s on p.product_id=s.product_id 
where s.year is not null
