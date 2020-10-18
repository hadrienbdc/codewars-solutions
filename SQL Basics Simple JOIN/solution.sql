select p.id, p.name, isbn, company_id, price, c.name as company_name
from products as p
inner join companies as c on p.company_id = c.id