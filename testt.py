import requests
import json
url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=10&offset=1'
response = requests.get(url)

rs = json.loads(response.text)
for data in rs['data']:
    print(data)

