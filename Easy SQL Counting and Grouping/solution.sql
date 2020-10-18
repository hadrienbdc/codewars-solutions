select race, count(*)
from demographics
group by race
order by count desc;