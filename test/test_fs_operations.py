import os
from unittest.mock import Mock, MagicMock, create_autospec

import pytest
import string

from smb.base import SharedFile

from config import config
from src.fs_operations import titlecase_names_in_current_dir

FAKE_SHARED_FOLDER = config.folder
FAKE_MUSIC_FOLDER = "/music"
VARIOUS_ARTISTS = "va"


@pytest.fixture
def empty_fs(fs):
    for letter in string.ascii_lowercase:
        path = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, letter)
        fs.create_dir(path)
    fs.create_dir(os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, VARIOUS_ARTISTS))


@pytest.fixture
def non_empty_fs(empty_fs, fs):
    artist_folder = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, "edward-ka spell")
    fs.create_dir(artist_folder)

    album_folder = os.path.join(artist_folder, "china doll")
    fs.create_dir(album_folder)

def test_titlecase_names(non_empty_fs, fs):
    music_folder = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER)

    conn = Mock()
    conn.listPath.side_effect = lambda shared_folder, current_dir: [
        create_autospec(SharedFile, instance=True) for _ in fs.listdir(current_dir)
    ]

    titlecase_names_in_current_dir(conn, music_folder)




