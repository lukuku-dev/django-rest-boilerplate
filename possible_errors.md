# Possible Errors

Problem 1: `django.db.utils.ProgrammingError: relation "users_user" does not exist`
Solution: 
```
python manage.py makemigrations users
python manage.py migrate
```

