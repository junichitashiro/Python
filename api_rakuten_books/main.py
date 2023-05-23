# ----------------------------------------
# モジュールのインポート
# ----------------------------------------
import requests
import pandas as pd


# ----------------------------------------
# 定数の設定
# ----------------------------------------
API_URL = 'https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404'
APP_ID = '取得したアプリIDを入力する'


# ----------------------------------------
# 検索クエリの設定
# ----------------------------------------
params = {
    'applicationId': APP_ID,
    'format': 'json',
    'keyword': '荒木飛呂彦'
}


# ----------------------------------------
# リクエスト結果の格納
# ----------------------------------------
res = requests.get(API_URL, params)
# ステータス確認用（200で成功）
res.status_code
result = res.json()

# itemsのリスト情報だけ格納し直す
items = result['Items']
len(items)  # 件数確認用


# ----------------------------------------
# データの整形
# ----------------------------------------
# そのままデータフレームに格納するとすべて1カラムに入ってしまうための編集
pd.DataFrame(items).head()
items = [item['Item'] for item in items]
df = pd.DataFrame(items)
df.head()

# 必要なカラム名を抽出する
df.columns
columns = ['title', 'itemCaption', 'itemPrice', 'availability']
df = df[columns]
df.head()

# カラム名を変更する
new_columns = ['商品', 'キャッチコピー', '価格', '販売可能']
df.columns = new_columns
df.head()

# データ型の変換が必要あるか確認する
df.dtypes

# データを商品名で並び替える
df.sort_values('商品', ascending=False)

# 統計量を確認する
df.describe()

# データを抽出する
df[df['価格'] > 2000]
