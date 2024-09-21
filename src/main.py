import logging

from connection import ConnectionAdapter

logging.basicConfig(level=logging.INFO)


def main():
    with ConnectionAdapter(user="test") as conn:
        # files = conn.listPath("Public", '/music')
        # for file in files:
        #     print(file.filename)
        pass

if __name__ == "__main__":
    main()
