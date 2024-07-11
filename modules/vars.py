import os

API_ID    = os.environ.get("API_ID", "21384105")
API_HASH  = os.environ.get("API_HASH", "df54a1f5ea9843313dccc0c2c2e44c0c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6149249287:AAGW1LycT7RPa8VfE4UFP_Pt5xHcbZqwTjs") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8089))  # Default to 8000 if not set
