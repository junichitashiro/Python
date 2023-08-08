import pandas as pd

def check_pattern(arr, pattern):
    return arr == pattern

# Excelファイルのパス
excel_file_path = '/path/to/master_file.xlsx'

# Excelファイルを読み込む
df = pd.read_excel(excel_file_path, dtype=str, header=None)

# 各パラメータを配列に格納する
param_array = ['24', '32', '36MB', '3.20GHz', '2.20GHz', '6.00GHz', 'DDR5-5600', 'DDR4-3200', '150W', 'LGA1700']

# パターン判定を行う
for idx, row in df.iterrows():
    pattern_name = row[0]
    pattern = row[1:].tolist()
    result = check_pattern(param_array, pattern)
    if result == True:
        print(f'合致する商品名: {pattern_name}')
