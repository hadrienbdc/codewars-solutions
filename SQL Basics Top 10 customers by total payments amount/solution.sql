select c.customer_id, email, count(*) as payments_count, cast(sum(amount) as float) as total_amount
from customer c
inner join payment p on c.customer_id = p.customer_id
group by c.customer_id
order by total_amount desc
limit 10;