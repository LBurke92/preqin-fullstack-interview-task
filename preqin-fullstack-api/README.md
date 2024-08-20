# Preqin API

This contains the API source code for the preqin fullstack interview task.
This is built using a Python + FastAPI Framework with SQLAlchemy as an ORM.

# Getting Started

You will need `python` installed on your machine, this application was built using Python `3.12.1` but any version `>= 3.10.0` should be fine.

You will need to install `fastapi`, `SQLAlchemy`,`pandas` `pytest` using pip. It is reccomended to use a virtual environment (venv) to set up these dependencies.

e.g. `pip install fastapi SQLAlchemy pandas pytest`

To first build the database you should execute the crud.py file as an application.

e.g `python3 -m investors.crud`

# Starting the application

To start the server you can simply run `fastapi dev FILE_PATH`.

e.g `fastapi dev ./investors/main.py`

The server should then be running on http://localhost:8000/

This will provide you with reload functionality thanks to something called `Uvicorn` not really sure what it does, but I saw some online hype about it.
