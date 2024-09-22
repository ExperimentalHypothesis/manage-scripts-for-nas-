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

logging.basicConfig(level=logging.INFO)


def rename_file_or_folder(conn, old_name, new_name):
    conn.rename(SHARED_FOLDER, old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.")



source_path = "path/to/source/file_or_directory"
destination_path = "path/to/destination/file_or_directory"

# Rename a file or directory
def rename_file_or_directory(source, new_name):
    new_path = os.path.join(os.path.dirname(source), new_name)
    shutil.move(source, new_path)
    print(f"Renamed '{source}' to '{new_path}'.")


def titlecase_names_in_dir(conn, current_dir: str):
    files = conn.listPath(SHARED_FOLDER, current_dir)
    for f in files:
        if f.filename == ".." or not f.isDirectory:
            continue
        if len(f.filename) == 1 or f.filename == "va":
            continue

        old_path = os.path.join(SHARED_FOLDER, MUSIC_FOLDER, f.filename)
        new_path = os.path.join(SHARED_FOLDER, MUSIC_FOLDER, f.filename.title().replace("-", " "))

        try:
            conn.rename(SHARED_FOLDER, old_path, new_path)
            logging.info(f"Renamed %s to % s", old_path, new_path)
        except Exception as e:
            logging.exception(f"Failed to rename '{old_path}' to '{new_path}': {e}")
