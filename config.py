import os
from typing import List

API_ID = os.environ.get("", "")
API_HASH = os.environ.get("", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("", ""))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("", ""))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("", "")
DB_NAME = os.environ.get("TeleApproveBot", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids
