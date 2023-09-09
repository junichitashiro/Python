import requests
import pandas as pd

# ----------------------------------------
# 定数の設定
# ----------------------------------------
API_URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
API_KEY = '取得したAPIキーを入力する'

# ----------------------------------------
# 検索クエリの設定
# ----------------------------------------
params = {
    'key': API_KEY,
    'keyword': '代々木上原',
    'count': 20,
    'format': 'json'
}

# ----------------------------------------
# リクエスト結果の格納
# ----------------------------------------
res = requests.get(API_URL, params=params)
# ステータス確認用（200で成功）
res.status_code
result = res.json()

# shopのリスト情報だけ格納し直す
items = result['results']['shop']

# ----------------------------------------
# 見やすいように必要なカラムを抽出する
# ----------------------------------------
df = pd.DataFrame(items)
df.columns
df = df[['name', 'address', 'non_smoking']]

# ----------------------------------------
# CSVに出力する
# ----------------------------------------
df.to_csv('hotpepper_shop_list.csv',index=False)
