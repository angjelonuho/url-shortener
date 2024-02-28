# URL Shortener
This is a simple URL shortener application built with FastAPI.

## Installation
1. Clone the repository
```sh
git clone https://github.com/angjelonuho/url-shortener.git
cd url-shortener || exit
```

2. Create a virtual environment and activate it (Optional)
```sh
python -m venv env
```
## On Windows:
```sh
.\env\Scripts\activate
```
## On Unix/MacOS:
```sh
source env/bin/activate
```
3. Install dependencies
```sh
pip install -r requirements.txt
```
4. Make sure setuptools is installed
```sh
pip install setuptools
```
>Before running the app, you need to set up a PostgreSQL database

# PostgreSQL setup
You need PostgreSQL installed and running.

The database username is 'postgres' and the password is 'hello'.

A database named 'urls' will be created.

Setup complete. Now you can run the app.

## Run the app
To run the app, execute the following command:
```sh
uvicorn main:app --reload
```
This will start the FastAPI development server. You can access the app at `http://localhost:8000`.