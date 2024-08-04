import pandas as pd
from datetime import datetime


def count(file_path: str, future_date: str, sheet_name: str = None) -> int:
    """
    与えられた日付までの営業日を返す関数  
    非営業日の一覧は別途ExcelファイルのA列に記載する  
    シート名の指定がない場合は先頭シートを対象とする  
    A1セルはヘッダ名として「非営業日」を記載する  
    A2セル以降にyyyy/m/d形式で非営業日を記載する  

    Args:
        file_path (str, pathlib.WindowsPath): Excelファイルのパス
        future_date (str): 未来日
        sheet_name (str, optional): シート名

    Returns:
        int: 未来日から非営業日を減算した日数
    """
    # Excelファイルを読み込む
    df = pd.read_excel(file_path, usecols='A')
    if sheet_name:
        df = pd.read_excel(file_path, sheet_name=sheet_name, usecols='A')
    else:
        df = pd.read_excel(file_path, usecols='A')

    # 非営業日をリストに変換する
    non_business_days = pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d')
    # 未来日を計算可能な形式に変換する
    future_date_obj = datetime.strptime(future_date, '%Y/%m/%d')

    # 非営業日一覧からすでに経過しているものを除く
    non_business_days = non_business_days[non_business_days >= datetime.today()]
    # 未来日までに設定されている非営業日を抽出する
    non_business_days_until_future = non_business_days[non_business_days <= future_date_obj]
    # 残った非営業日数
    non_business_days_count = len(non_business_days_until_future)

    # 未来日までの日数を計算する　※営業日の考え方で加算日を調整
    total_days = (future_date_obj - datetime.today()).days + 1
    # 非営業日を減算し営業日数を計算する
    business_days = total_days - non_business_days_count

    return business_days
