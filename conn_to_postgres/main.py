import psycopg2

# PostgreSQLへの接続設定
def conn_to_postgres():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='postgres',
            password='password',
            host='127.0.0.1',
            port='5432'
        )
        return conn
    except Exception as e:
        print('Error: データベースに接続できませんでした')
        print(e)
        return None

# テーブルからデータを取得する
def get_data_from_table(conn, table_name, column_name, value):
    try:
        cursor = conn.cursor()
        query = f'SELECT * FROM {table_name} WHERE {column_name} = %s;'
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print('Error: テーブルからデータを取得できませんでした')
        print(e)
        return []

if __name__ == '__main__':
    conn = conn_to_postgres()
    if conn:
        table_name = 'test_table'
        column_name = 'menu'
        value = 'Espresso coffee'

        data = get_data_from_table(conn, table_name, column_name, value)

        if data:
            for row in data:
                print(row)

        # データベースとの接続を終了する
        conn.close()
