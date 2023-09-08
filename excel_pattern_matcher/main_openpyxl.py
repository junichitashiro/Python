import openpyxl

def check_pattern(arr, pattern):
    return arr == pattern

if __name__ == '__main__':
    # Excelファイルのパス
    excel_file_path = '/path/to/master_file.xlsx'

    # Excelファイルを開く
    workbook = openpyxl.load_workbook(excel_file_path, data_only=False)
    sheet = workbook.active

    # 各パラメータを配列に格納する
    param_array = ['24', '32', '36MB', '3.20GHz', '2.20GHz', '6.00GHz', 'DDR5-5600', 'DDR4-3200', '150W', 'LGA1700']

    # パターン判定を行う
    for row in sheet.iter_rows(min_row=2, values_only=True):    # 1行目はヘッダーとする
        pattern_name = row[0]
        pattern = list(row[1:])
        pattern = [str(cell) for cell in pattern]  # セルの値を文字列に変換
        result = check_pattern(param_array, pattern)
        if result == True:
            print(f'合致する商品名: {pattern_name}')

    # ファイルを閉じる
    workbook.close()
