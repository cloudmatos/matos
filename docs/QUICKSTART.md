[<img src="../images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

## Dependencies

- [python 3.8](https://www.python.org/) Python language
- [flask 2.0.2](https://flask.palletsprojects.com/en/2.0.x/): Python server
- [Other ...](../requirements.txt)

## Setup Process
- Create a local directory and navigate to it
- Clone the matos code to the local directory
- Setup a virtual environment: python -m venv /path/to/env
- Activate virtual environment: source /path/to/env/activate
- Setup requirements: pip install -r requirements.txt
- Run flask server: python -m flask run (Default Flask Part)
- Unittests: python -m unittest

## Execution
- Home API: Visit http://localhost:5000/api
- Resources API: - http://localhost:5000/resources/gcp
- Documentation: Visit http://localhost:5000/apidocs

## General Comments
- Flask app file is named as matos.py
