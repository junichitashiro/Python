import pandas as pd
from pathlib import Path


def check_excel_file(file_path: Path, check_sheet_names: list = ['Sheet1']) -> bool:
    """
    指定されたExcelファイルとシートの存在を確認し、読み込み可能かを検証する関数

    Args:
        file_path (Path): チェックするExcelファイルのパス（Pathオブジェクト）
        check_sheet_names (list): 存在を確認したいシート名のリスト

    Returns:
        bool: ファイルとシートが存在し読み込み可能であれば True、エラーがあれば False
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f'エラー: ファイルが見つかりません -> {file_path}')
        return False

    try:
        with pd.ExcelFile(file_path) as xlsx:
            print(f'ファイルを正常に読み込みました -> {file_path.name}')

            sheet_names = xlsx.sheet_names
            sheet_is_exist = {sheet: sheet in sheet_names for sheet in check_sheet_names}

            if not all(sheet_is_exist.values()):
                print('エラー: 存在しないシートがあります')
                print(sheet_is_exist)
                return False

            print('チェック対象シートはすべて存在します')
            print(check_sheet_names)
            return True

    except FileNotFoundError:
        print(f'エラー: ファイルが見つかりません -> {file_path}')
    except PermissionError:
        print(f'エラー: ファイルへのアクセスが拒否されました -> {file_path}')
    except ValueError as e:
        print(f'エラー: {e}')
    except Exception as e:
        print(f'予期しないエラーが発生しました: {e}')

    return False
