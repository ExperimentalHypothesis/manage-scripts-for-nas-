from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    user = os.getenv("USER")
    password = os.getenv("PWD")
    client = os.getenv("CLIENT")
    server = os.getenv("SERVER")
    ip = os.getenv("IP")
    folder = os.getenv("FOLDER")
    port = os.getenv("PORT")


config = Config()
