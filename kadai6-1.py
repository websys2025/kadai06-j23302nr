import requests

APP_ID = "4546048a7a06f7af33719c507b3ec4ea0e0acc8d"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003410379",  #国勢調査 時系列データ 男女，年齢，配偶関係 
    "cdArea": "11000",  #埼玉県
    "cdTime": "2020000000",  #2020年
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)