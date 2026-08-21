-- Write your query below
select s.seller_name
from seller s
--seller with no sale in 2020
where s.seller_id not in(
    select o2.seller_id
    from orders o2
    WHERE sale_date >= '2020-01-01' AND sale_date <= '2020-12-31')

order by seller_name 