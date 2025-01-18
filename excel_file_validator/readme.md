# Excelファイル読み込み時のチェック処理

## excel_file_validator.py

### 指定されたExcelファイルとシートの存在を確認し、読み込み可能かを検証する関数

### 処理内容

1. Excelファイルが存在するか確認する
2. 存在する場合はファイルを読み込んでシートが存在するか確認する
3. ファイルとシートの存在チェック結果、読み込みチェック結果を返す

### プログラムの定義

* 関数名: check_excel_file
* 引数
  * file_path (str): チェックするExcelファイルのパス
  * sheet_name (str, optional): 存在を確認するシート名（デフォルトは'Sheet1'）
* 戻り値
  * bool: ファイルとシートが存在し読み込み可能であれば True、そうでなければ False

### 使い方

* カレントディレクトリに配置したファイルを対象とした場合のサンプル

```python
import excel_file_validator
from pathlib import Path

file_path = Path.cwd() / 'test.xlsx'
sheet_name = 'Sheet1'
result = excel_file_validator.check_excel_file(file_path, sheet_name)
print('チェック結果:', result)
```
