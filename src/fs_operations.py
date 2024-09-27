# Module for performing filesystem operations like
#  - moving
#  - renaming
#  - deleting

import os
import shutil

from config import config
from log import setup_logger


SHARED_FOLDER = config.folder
VARIOUS_ARTISTS = "VA"


logger = setup_logger()


def move_duplicates(conn, old_dir):
    # Define new directory path
    new_dir = old_dir.replace("music", "music duplicated albums")

    # Split the new directory path into components
    new_dir_parts = new_dir.split('/')

    # Create each part of the new directory path
    current_path = ''
    for part in new_dir_parts:
        current_path = os.path.join(current_path, part)
        try:
            conn.createDirectory(SHARED_FOLDER, current_path)  # Create each directory
        except Exception as e:
            print(f"Directory {current_path} already exists or cannot be created")

    # Now proceed to move files
    try:
        print(f"Moving duplicated dir to {new_dir}")
        files = conn.listPath(SHARED_FOLDER, old_dir)

        for file in files:
            if file.isDirectory:
                continue  # Skip subdirectories for now

            source_file = os.path.join(old_dir, file.filename)
            destination_file = os.path.join(new_dir, file.filename)

            # Copy file from old_dir to new_dir
            with open('temp_file', 'wb') as temp_file:
                conn.retrieveFile(SHARED_FOLDER, source_file, temp_file)  # Download file

            with open('temp_file', 'rb') as temp_file:
                conn.storeFile(SHARED_FOLDER, destination_file, temp_file)  # Upload file to new location

        # Optionally delete original files after copying
        for file in files:
            if not file.isDirectory:
                conn.deleteFiles(SHARED_FOLDER, os.path.join(old_dir, file.filename))

        try:
            conn.deleteDirectory(SHARED_FOLDER, old_dir)
            print(f"Deleted original directory: {old_dir}")
        except Exception as e:
            print(f"Failed to delete original directory {old_dir}")

        print(f"Moved {old_dir} to {new_dir}")

    except Exception as err:
        with open("errors.txt", "a") as errors:  # Append mode for errors
            print(f"Error moving {old_dir}: {err}", file=errors)


def titlecase_directory_names(conn, current_dir: str):
    """
    Recursively titlecase directory names.
    When run on 'Music' it first title cases the artist name, then its album names.

    The folder structure is like this:
    Public/
        Music/
            a
            b
            c
    """
    files = conn.listPath(SHARED_FOLDER, current_dir)

    for f in files:
        if f.filename == "." or f.filename == ".." or not f.isDirectory:
            continue

        old_dir = os.path.join(SHARED_FOLDER, current_dir, f.filename)
        new_dir = os.path.join(SHARED_FOLDER, current_dir, f.filename.title().replace("-", " "))

        try:
            conn.rename(SHARED_FOLDER, old_dir, new_dir)
            print(f"Renamed {old_dir} to {new_dir}")
            titlecase_directory_names(conn, new_dir)
        except Exception as e:
            with open("errors.txt", "w") as errors:
                print(f"Error: directory {old_dir} cannot be renamed because the same name already exists", file=errors)

            move_duplicates(conn, old_dir)


