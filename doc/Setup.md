## Project Setup

### Setup for development

1. install pre-commit, make sure this lip installed on local development pc

```
pip install pre-commit
```

2. install python code linter

```
pip install ruff
```

3. run precommit commands

```
pre-commit clean
pre-commit install
pre-commit run --all-files
```


4. setup migrations
   cd backend/api_server
   install alembic
   alembic revision --autogenerate -m "Added ai tables 1"

   alembic upgrade head


5. run tests
```
cd backend 

python -m pytest tests/ -v -s

-s to show all print
-v verbose to show all detail
```