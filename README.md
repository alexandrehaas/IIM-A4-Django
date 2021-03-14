# IIM-A4-Django

Projet Django CV

## Pré Requis

- python3
- docker-compose

```
> git clone https://github.com/alexandrehaas/IIM-A4-Django.git
> cd IIM-A4-Django
```

### Windows 10

```ps1
> python -m venv .virtualenvs
> .virtualenvs\Scripts\activate.ps1
```

### Unix / MacOS

```bash
> python3 -m venv .virtualenvs
> source .virtualenvs/bin/activate
```

## Installation

```
> pip install -r requirements.txt
> docker-compose up
> cd project
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver
```
