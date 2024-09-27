import logging
import os.path
from pathlib import Path

from config import config
from connection import ConnectionAdapter
from src.fs_operations import titlecase_directory_names

logging.basicConfig(level=logging.INFO)


MUSIC_FOLDER = "/music"

def main():
    with ConnectionAdapter(user="test") as conn:

        curr_dir = os.path.join(MUSIC_FOLDER, "S")
        titlecase_directory_names(conn, curr_dir)


if __name__ == "__main__":
    main()
