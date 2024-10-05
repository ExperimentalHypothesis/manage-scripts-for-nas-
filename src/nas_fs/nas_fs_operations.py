# Module for performing filesystem operations like
#  - moving
#  - renaming
#  - deleting

import os

from config import config
import logging

SHARED_FOLDER = config.folder
VARIOUS_ARTISTS = "VA"



def move_dirs_on_nas(root):
    with nas_connection() as conn:
        for folder in conn.listPath("Public", root):
            if folder.filename.startswith(".") or folder.filename.startswith("..") or not folder.isDirectory:
                continue
            if folder.filename in ascii_uppercase:
                continue

            print(f"folder is {folder.filename}")
            first_letter = folder.filename[0]
            print(f"first letter is {first_letter}")

            src = os.path.join(root, folder.filename)
            dst = os.path.join(root, first_letter, folder.filename)

            try:
                print(f"Try moving src dir {src} to dst dir {dst}")
                conn.rename("Public", src, dst)
            except Exception as e:
                for subfolder in conn.listPath("Public", src):
                    if subfolder.filename.startswith("."):
                        continue
                    sub_src = os.path.join(src, subfolder.filename)
                    sub_dst = os.path.join(dst, subfolder.filename)
                    try:
                        conn.rename("Public", sub_src, sub_dst)
                    except Exception as e:
                        print("Album exists, skipping")


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