select coalesce(chr(cast((sum(ascii(letter) - 96) - 1) % 26 as int) + 97), 'z') as letter
from letters;