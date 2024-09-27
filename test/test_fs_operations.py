import os
from unittest.mock import Mock, MagicMock, create_autospec

import pytest
import string

from smb.base import SharedFile

from config import config
from src.fs_operations import titlecase_directory_names

FAKE_SHARED_FOLDER = config.folder
FAKE_MUSIC_FOLDER = "/music"
VARIOUS_ARTISTS = "va"


@pytest.fixture
def empty_fs(fs):
    for letter in string.ascii_lowercase:
        path = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, letter)
        fs.create_dir(path)
    fs.create_dir(os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, VARIOUS_ARTISTS))


def test_titlecase_names(empty_fs, fs):
    # Arrange data
    # - add one artist name to empty filesystem
    artist_name = "edward-ka spell"
    artist_folder = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, artist_name)
    fs.create_dir(artist_folder)

    # - add one album
    album_name = "china doll"
    album_folder = os.path.join(artist_folder, album_name)
    fs.create_dir(album_folder)

    assert fs.exists(album_folder), f"Expected album folder '{album_folder}' does not exist."
    assert fs.exists(artist_folder), f"Expected album folder '{album_folder}' does not exist."

    music_folder = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER)

    # Mock the call to listPath
    conn = Mock()
    conn.listPath.side_effect = lambda shared_folder, current_dir: [
        Mock(filename=name, isDirectory=True) for name in fs.listdir(current_dir)
    ]

    # Act
    titlecase_directory_names(conn, music_folder)

    artist_name_old = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, artist_name)
    artist_name_new = os.path.join(FAKE_SHARED_FOLDER, FAKE_MUSIC_FOLDER, artist_name.title().replace("-", " "))
    conn.rename.assert_called_once_with(FAKE_SHARED_FOLDER, artist_name_old, artist_name_new)
    conn.rename.assert_called_once_with(FAKE_SHARED_FOLDER, artist_name_old, artist_name_new)
