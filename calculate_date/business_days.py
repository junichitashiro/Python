import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Optional


def non_business_days_read(file_path: Path, sheet_name: Optional[str] = None) -> pd.DataFrame:
    """
    Excelに記載した非営業日一覧をデータフレームに変換して返す関数  
    A1セルはヘッダ名として「非営業日」を記載する  
    A2セル以降にyyyy/m/d形式で非営業日を記載する

    Args:
        file_path (Path): Excelファイルのパス
        sheet_name (Optional[str], optional): 読み込むシート名、省略時（None）は先頭のシートを使用する

    Returns:
        pd.DataFrame: 非営業日一覧のデータフレーム
    """
    if sheet_name:
        df = pd.read_excel(file_path, sheet_name=sheet_name, usecols='A')
    else:
        df = pd.read_excel(file_path, usecols='A')

    df['非営業日'] = pd.to_datetime(df['非営業日']).dt.strftime('%Y/%m/%d')

    return df


def count(file_path: Path, future_date: str, sheet_name: Optional[str] = None) -> int:
    """
    与えられた日付までの営業日数を返す関数  
    非営業日の一覧は別途Excelファイルに記載する

    Args:
        file_path (Path): Excelファイルのパス
        future_date (str): 未来日
        sheet_name (Optional[str], optional): 読み込むシート名、省略時（None）は先頭のシートを使用する

    Returns:
        int: 未来日から非営業日を減算した日数
    """
    # Excelファイルから非営業日一覧を取得する
    df = non_business_days_read(file_path, sheet_name)

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


def calc_minus(file_path: Path, target_date: str, days_to_subtract: int, sheet_name: Optional[str] = None) -> str:
    """
    日付に対して指定した営業日数を引いた日付を返す関数  
    非営業日の一覧は別途Excelファイルに記載する  
    指定する日付が非営業日だった場合はその旨を知らせるメッセージを返す

    Args:
        file_path (Path): Excelファイルのパス
        target_date (str): ターゲットとなる日付
        days_to_subtract (int): ターゲットの日付から引く営業日数
        sheet_name (Optional[str], optional): 読み込むシート名、省略時（None）は先頭のシートを使用する

    Returns:
        str: 指定した日付から指定した営業日数を引いた日付
    """
    # Excelファイルから非営業日一覧を取得する
    df = non_business_days_read(file_path, sheet_name)

    # 非営業日をリストに変換する
    non_business_days = pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d')
    # 指定する未来日と比較できる形式に変換する
    non_business_days = non_business_days.apply(lambda x: x.strftime('%Y/%m/%d')).tolist()
    target_date_obj = datetime.strptime(target_date, '%Y/%m/%d')

    # 指定日のチェック
    if target_date in non_business_days:
        return '指定した日付は非営業日です'

    # 営業日数を計算
    while days_to_subtract > 0:
        target_date_obj -= pd.Timedelta(days=1)
        if target_date_obj.strftime('%Y/%m/%d') not in non_business_days:
            days_to_subtract -= 1

    result_date = target_date_obj.strftime('%Y/%m/%d')

    return result_date


def calc_plus(file_path: Path, target_date: str, days_to_addition: int, sheet_name: Optional[str] = None) -> str:
    """
    日付に対して指定した営業日数を足した日付を返す関数  
    非営業日の一覧は別途Excelファイルに記載する  
    指定する日付が非営業日だった場合はその旨を知らせるメッセージを返す

    Args:
        file_path (Path): Excelファイルのパス
        target_date (str): ターゲットとなる日付
        days_to_addition (int): ターゲットの日付から引く営業日数
        sheet_name (Optional[str], optional): 読み込むシート名、省略時（None）は先頭のシートを使用する

    Returns:
        str: 指定した日付から指定した営業日数を引いた日付
    """
    # Excelファイルから非営業日一覧を取得する
    df = non_business_days_read(file_path, sheet_name)

    # 非営業日をリストに変換する
    non_business_days = pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d')
    # 指定する未来日と比較できる形式に変換する
    non_business_days = non_business_days.apply(lambda x: x.strftime('%Y/%m/%d')).tolist()
    target_date_obj = datetime.strptime(target_date, '%Y/%m/%d')

    # 指定日のチェック
    if target_date in non_business_days:
        return '指定した日付は非営業日です'

    # 営業日数を計算
    while days_to_addition > 0:
        target_date_obj += pd.Timedelta(days=1)
        if target_date_obj.strftime('%Y/%m/%d') not in non_business_days:
            days_to_addition -= 1

    result_date = target_date_obj.strftime('%Y/%m/%d')

    return result_date
