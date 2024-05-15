from os import environ, path
from dotenv import load_dotenv

class Config: 
    RECEIVER_ADDRESS = environ.get("RECEIVER_ADDRESS")