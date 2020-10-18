select pokemon_name, str * multiplier as modifiedStrength, element
from pokemon p 
join multipliers m on element_id = m.id
where str * multiplier >= 40
order by modifiedStrength desc;