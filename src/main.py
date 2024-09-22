import logging
from pathlib import Path

from config import config
from connection import ConnectionAdapter
from src.fs_operations import titlecase_names_in_dir

logging.basicConfig(level=logging.INFO)



def main():
    with ConnectionAdapter(user="test") as conn:

        titlecase_names_in_dir(conn, "music")

        pass


if __name__ == "__main__":
    main()
