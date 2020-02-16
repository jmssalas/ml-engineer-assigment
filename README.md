# ml-engineer-assigment

### How to run API server
1. Run the `migrate` and `loaddata` commands

`python mlapi/manage.py migrate`

`python mlapi/manage.py loaddata mlapi/models/fixtures/*`

2. Run the server:

`python mlapi/manage.py runserver`