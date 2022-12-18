
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive', 
]

cred = ServiceAccountCredentials.from_json_keyfile_name('google7sob/abdoomankeys.json', scopes)
file = gspread.authorize(cred)
sheet = file.open('test').sheet1