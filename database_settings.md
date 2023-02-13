# Django Database Settings

## PostgreSQL [DEFAULT]

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('SQL_DBNAME'),
        'USER': env('SQL_USERNAME'),
        "PASSWORD": env('SQL_PASSWORD'),
        "HOST": env('SQL_HOSTNAME'),
        "PORT": env('SQL_PORT')


    }
}
```
## MySQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('SQL_DBNAME'),
        'USER': env('SQL_USERNAME'),
        "PASSWORD": env('SQL_PASSWORD'),
        "HOST": env('SQL_HOSTNAME'),
        "PORT": env('SQL_PORT')
    }
}
```

## SQLite

```python
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Sqlite Memory

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
```
