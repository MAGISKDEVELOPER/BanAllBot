
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_KEY = config("21124451", default=6, cast=int)
    API_HASH = config("d0c75e0e8ae1f79ddad10a033411f9ed", None)
    TOKEN = config("6246031074:AAHtUpc0r-ynm1KnmP56yvGMcWp7SWpBvRU", None)
    OWNER_ID = list(map(int, getenv("6161624470").split()))
