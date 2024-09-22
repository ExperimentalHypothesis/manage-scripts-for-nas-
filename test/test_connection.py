from unittest.mock import patch, Mock

import pytest

from config import config
from src.connection import ConnectionAdapter


def test_init():
    conn = ConnectionAdapter(user="test")
    assert conn.user == "test"

    conn = ConnectionAdapter()
    assert conn.user == "lukas.kotatko"


def test_enter_exit(mocker):
    mock_instance = Mock()
    mocker.patch("src.connection.SMBConnection", return_value=mock_instance)

    # test enter
    with ConnectionAdapter() as conn:
        assert conn is mock_instance
    mock_instance.connect.assert_called_once_with(config.ip, config.port)

    # test exit
    ConnectionAdapter.__exit__(conn, None, None, None)
    mock_instance.close.assert_called_once()

