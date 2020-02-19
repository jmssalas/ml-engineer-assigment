# ML Engineer Assigment

## Exercises
### First exercise
This exercise has been resolved using Jupyter Notebook with Anaconda distribution 
(Anaconda 2019.10 for Linux Installer, Python 3.7 version).

The file is `src/first-exercice.ipynb` and `finalized_model.sav` is the ML model
created at the end of the notebook. The file `src/first-exercise.html` is the 
notebook in HTML version.


### Second exercise
This exercise has been resolved using Python 3.7.4 and the requirements specified 
in `requirements.txt` file.

The file is `src/second-exercise.py` and to execute it, you should be in `src/` folder 
and run:

`python second-exercise.py`

This file has the relevant constants:

- `LOCAL_SERVER_URL`: The URL of local API server
- `EXTERNAL_SERVER_URL`: The URL of online API server
- `EXTERNAL`: Indicates whether run the script using the online API server.
- `BLOCK_SIZE`: Block size used to call the API server. This constant is used to not 
send all dataset to the API.

## API
The API server is in `mlapi` folder and it is a Django 2.1.1 project.

### How to run API server
1. Run the `migrate` and `loaddata` commands

`python manage.py migrate`

`python manage.py loaddata mlapi/models/fixtures/*`

2. Run the server:

`python manage.py runserver`

### API endpoints
The API has just one endpoint:

`POST /api/v1/predict`

that required a JSON body like this:

```json
[
	{
	    "user_id": 1188693,
	    "join_date": "2020-07-01 00:00:03",
	    "hidden": 1,
	    "STV": 0.3975,
	    "target": 0.3975,
	    "credit_card_level": "prepaid",
	    "is_lp": 1231,
	    "aff_type": "PPS",
	    "is_cancelled": 1,
	    "country_segment": "US"
	}
        ...
]
```
where `user_id` and `join_date` fields must be informed.