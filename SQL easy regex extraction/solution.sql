SELECT name, greeting, replace(substring(greeting, '#[\d]+'), '#', '') as user_id
FROM greetings;