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
   install alembic
   alembic revision --autogenerate -m "Added ai tables 1"

   alembic upgrade head