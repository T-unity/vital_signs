import os
from dotenv import load_dotenv
import requests

# .envファイルを読み込む
load_dotenv()

url = 'https://api.ouraring.com/v2/usercollection/daily_activity'
params = {
    'start_date': '2024-06-05',
    'end_date': '2024-06-06'
}
headers = {
    'Authorization': f"Bearer {os.getenv('API_TOKEN')}"
}
response = requests.request('GET', url, headers=headers, params=params)
print(response.text)
