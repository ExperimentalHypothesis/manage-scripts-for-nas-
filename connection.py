import logging

from smb.SMBConnection import SMBConnection
from config import config


class ConnectionAdapter:

    def __init__(self, *, user=config.user):
        self.user = user

    def __enter__(self):
        logging.info(f"Trying to connecting to NAS server: {config.ip} for user {self.user}")

        try:
            self.conn = SMBConnection(self.user,
                                      config.password,
                                      config.client,
                                      config.server,
                                      use_ntlm_v2=True)
            self.conn.connect(config.ip, config.port)
            logging.info(f"Connecting to NAS server: {config.ip} was successful.")
            return self.conn
        except Exception as exc:
            logging.exception(f"Connection to NAS server: {config.ip} failed due to {exc}")

    def __exit__(self, exc_type, exc_value, exc_tb):
        if hasattr(self, "conn"):
            try:
                self.conn.close()
                logging.info(f"Connection to NAS server: {config.ip} was closed.")
            except Exception as exc:
                logging.exception(f"Failed to close connection to NAS server {config.ip} due to {exc}")