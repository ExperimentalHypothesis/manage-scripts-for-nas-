# Module for performing filesystem operations like
#  - moving
#  - renaming
#  - deleting


import logging
import os
import shutil
from pathlib import Path
import logging
from config import config


SHARED_FOLDER = config.folder
MUSIC_FOLDER = "/music"
VARIOUS_ARTISTS = "va"

logging.basicConfig(level=logging.INFO)


def titlecase_names_in_current_dir(conn, current_dir: str):
    files = conn.listPath(SHARED_FOLDER, current_dir)
    # print("DASDADAD")
    # print(files)
    for f in files:
        print(f, type(f))
        print(f, dir(f))
        # if f.filename == ".." or not f.isDirectory:
        #     continue
        # if len(f.filename) == 1 or f.filename == VARIOUS_ARTISTS:
        #     continue
        #
        # old_path = os.path.join(SHARED_FOLDER, MUSIC_FOLDER, f.filename)
        # new_path = os.path.join(SHARED_FOLDER, MUSIC_FOLDER, f.filename.title().replace("-", " "))
        #
        # try:
        #     conn.rename(SHARED_FOLDER, old_path, new_path)
        #     logging.info(f"Renamed %s to % s", old_path, new_path)
        #     # titlecase_names_in_current_dir(conn, new_name)
        # except Exception as e:
        #     logging.exception(f"Failed to rename '{old_path}' to '{new_path}': {e}")
