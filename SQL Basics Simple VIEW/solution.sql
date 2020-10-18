create view members_approved_for_voucher as
  select m.id, m.name, m.email, sum(p.price) as total_spending
  from sales s
  inner join members m on s.member_id = m.id
  inner join products p on s.product_id = p.id
  where s.department_id in (
      select s.department_id
      from sales s
      inner join products p on s.product_id = p.id
      group by s.department_id
      having sum(p.price) > 10000)
  group by m.id
  having sum(p.price) > 1000
  order by m.id;

select * from members_approved_for_voucher;