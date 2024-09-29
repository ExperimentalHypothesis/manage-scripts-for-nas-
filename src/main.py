import logging
import os.path
from pathlib import Path

from config import config
from connection import ConnectionAdapter
from src.fs_operations import titlecase_directory_names, move_dirs_on_nas

logging.basicConfig(level=logging.INFO)


MUSIC_FOLDER = "/music duplicated albums"

def main():
    with ConnectionAdapter(user="test") as conn:

        # curr_dir = os.path.join(MUSIC_FOLDER, "G")
        titlecase_directory_names(conn, MUSIC_FOLDER)

    move_dirs_on_nas(MUSIC_FOLDER)


if __name__ == "__main__":
    main()
