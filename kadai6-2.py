import requests

API_URL  = "https://opendata.city.minato.tokyo.jp/dataset/e9c32c87-a106-4827-8623-b112f190866b/resource/0d879c8a-67d4-42a9-87a4-abfc3df6a2a8/download/tenpohanbai.json"

#東京都港区の医薬品販売業（店舗販売業）一覧
#店舗の一覧とそれぞれの情報のデータ
#店舗ごとのデータ：業態、施設名称、施設所在地、施設方書、施設電話番号、許可番号、許可開始日

params = {}  



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)