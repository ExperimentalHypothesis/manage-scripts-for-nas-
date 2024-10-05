import os
from smb.SMBConnection import SMBConnection
import logging

logger = logging.getLogger("x")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

def connect_to_nas():
    # conn = SMBConnection(username, password, "local_machine", "nas_device", use_ntlm_v2=True)
    # conn.connect(nas_ip)
    logger.warning("Connected")
    return


if __name__ == "__main__":
    connect_to_nas()
