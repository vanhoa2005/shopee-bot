import gspread
from google.oauth2.service_account import Credentials
import os
import json

# ====== GOOGLE SHEET CONNECT ======
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client = gspread.authorize(creds)

SHEET_ID = "DÁN_SHEET_ID_CỦA_BẠN_VÀO_ĐÂY"
sheet = client.open_by_key(SHEET_ID).sheet1
# ==================================

sheet.append_row(["BOT RUN OK", "GitHub", "Success"])
