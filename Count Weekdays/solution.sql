create or replace function weekdays(date, date)
  returns integer as
$func$
select count(*)::int
from generate_series(least($1, $2), greatest($1, $2), interval '1d') days
where extract(isodow from days) < 6;
$func$  
language sql 
immutable;