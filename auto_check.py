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

SHEET_ID = "1jg8l5M3-IXLdWKgBJLcBIN_NqsbTMumMy1W2y1_TdYI"
sheet = client.open_by_key(SHEET_ID).sheet1
# ==================================

sheet.append_row([
    product_name,
    price,
    link
])
