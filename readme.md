# Flask Playground

Create `.env` in root directory
```ini
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
```

Use `python-dotenv` module to launch Flask reading `.env` file
```commandline
python -m dotenv run flask run
```
