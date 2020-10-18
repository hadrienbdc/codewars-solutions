select project, regexp_replace(address, '[\d]', '', 'g') as letters, 
regexp_replace(address, '[^\d]', '', 'g') as numbers
from repositories;