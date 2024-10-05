from connection import ConnectionAdapter

import logging

logger = logging.getLogger(__name__)

MUSIC_FOLDER = "/music duplicated albums"

def main():
    with ConnectionAdapter(user="test") as conn:



if __name__ == "__main__":
    main()
