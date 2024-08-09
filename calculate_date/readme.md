# 概要

各種日付の計算を関数にまとめたもの

## 処理内容

---

### date_difference.py

与えられた2つの日付データから日数の差を計算して返す

* 関数名: diff
* 引数
  * date1(str)
  * date2(str)
* 形式: 'yyyy/m/d' または 'yyyy/mm/dd'
* 戻り値
  * int: 日数

#### 使い方

```python
import date_difference as dd

date1 = '2024/8/5'
date2 = '2024/8/6'
print(dd.diff(date1, date2))
```

#### 実行結果

> 1

---

### compare_dates.py

与えられた2つの日付データからどちらが未来日であるか判定して結果を返す

* 関数名: compare
* 引数
  * date1(str)
  * date2(str)
* 形式: 'yyyy/m/d' または 'yyyy/mm/dd'
* 戻り値
  * str: 判定結果のメッセージ

#### 使い方①

```python
import compare_dates as cd

date1 = '2024/08/10'
date2 = '2024/08/25'
print(cd.compare(date1, date2))
```

#### 実行結果①

> 2024/08/25 の方が未来日です

#### 使い方②

```python
import compare_dates as cd

date1 = '2024/08/25'
date2 = '2024/08/25'
print(cd.compare(date1, date2))
```
#### 実行結果②

> 同じ日付です

---

### business_days.py

与えられた日付（未来日）までの営業日を返す関数

* 関数名: count
* 引数
  * file_path (str, pathlib.WindowsPath): Excelファイルのパス
  * future_date (str): 未来日
  * sheet_name (str, optional): シート名
* 形式: 'yyyy/m/d' または 'yyyy/mm/dd'
* 戻り値
  * int: 未来日から非営業日を減算した日数

#### インプットとなるExcelファイル

* 非営業日の一覧をExcelファイルのA列に記載する
* シート名の指定がない場合は先頭シートを対象とする
* A1セルはヘッダ名として **非営業日** を記載する
* A2セル以降にyyyy/m/d形式で非営業日を記載する
  * 入力例

    |       |     A     |
    | :---: | :-------: |
    |   1   | 非営業日  |
    |   2   | 2024/1/1  |
    |   3   | 2024/1/6  |
    |   4   | 2024/1/7  |
    |   5   | 2024/1/8  |
    |   6   | 2024/1/13 |
    |   7   | 2024/1/14 |
    |   8   | 2024/1/20 |

#### 使い方①

2024年8月4日に実行

```python
import business_days as bd
from pathlib import Path

file_path = Path.cwd() / 'non_business_days.xlsx'
future_date = '2024/08/13'
print(bd.count(file_path, future_date))
```

#### 実行結果①

> 6

#### 使い方②

シート名（Sheet1）を指定する場合

```python
import business_days as bd
from pathlib import Path

file_path = Path.cwd() / 'non_business_days.xlsx'
sheet_name = 'Sheet1'
future_date = '2024/08/13'
print(bd.count(file_path, future_date, sheet_name))
```

#### 実行結果②

> 6
