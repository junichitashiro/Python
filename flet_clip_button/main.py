import flet as ft
import pandas as pd


def main(page: ft.Page):
    # ページ全体のレイアウト
    page.window_width=400
    page.window_height=600
    page.scroll=True

    # クリップボードにテキストをコピーする関数
    def copy_to_clipboard(e):
        text = e.control.text
        page.set_clipboard(text)
        page.snack_bar = ft.SnackBar(ft.Text(f'Copied {text} to clipboard'))
        page.snack_bar.open = True
        page.update()

    # Excelファイルからデータを読み込む
    df = pd.read_excel('data.xlsx', usecols='A,B', header=None, dtype=str)

    # ボタンを表示するためのリスト
    buttons = []

    # データフレームの各行からボタンを作成し、リストに追加
    for index, row in df.iterrows():
        col_a_button = ft.ElevatedButton(text=row[0], on_click=copy_to_clipboard)
        col_b_button = ft.ElevatedButton(text=row[1], on_click=copy_to_clipboard)
        buttons.append(ft.Row([col_a_button, col_b_button]))

    # ページにボタンを追加
    for row in buttons:
        page.add(row)


# アプリを実行
ft.app(target=main)
