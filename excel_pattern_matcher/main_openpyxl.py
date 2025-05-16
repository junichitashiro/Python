import openpyxl
from pathlib import Path
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook
from typing import Any


def check_pattern(arr, pattern) -> Any:
    return arr == pattern


# Excelファイルの読み込み
excel_file_path = Path('/path/to/master_file.xlsx')
workbook: Workbook = openpyxl.load_workbook(excel_file_path, data_only=False)

# activeシートがNoneでないことを確認（型チェックツール対策）
sheet_raw = workbook.active
assert sheet_raw is not None, "アクティブなシートが取得できませんでした。"
sheet: Worksheet = sheet_raw

# 比較するパラメータの格納
param_array = ['24', '32', '36MB', '3.20GHz', '2.20GHz', '6.00GHz', 'DDR5-5600', 'DDR4-3200', '150W', 'LGA1700']

# パターン判定を行う
for row in sheet.iter_rows(min_row=2, values_only=True):
    pattern_name = row[0]
    pattern = list(row[1:])
    pattern = [str(cell) for cell in pattern]  # セルの値を文字列に変換
    result = check_pattern(param_array, pattern)
    if result:
        print(f'合致する商品名: {pattern_name}')

# ファイルを閉じる
workbook.close()
