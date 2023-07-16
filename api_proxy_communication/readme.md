# 処理概要

proxy（Tor）経由でAPI通信を実行する

## 処理内容

1. Torを起動する
2. プロキシを使用せずAPIリクエストを実行する
3. プロキシを使用して同じAPIリクエストを実行する

### 事前準備

* Windows版Torを使用する
* [公式サイト](https://www.torproject.org/ja/download/tor/)からエキスパートバンドルファイルをダウンロードして任意のフォルダに展開しておく

### 対象API

* https://ipinfo.io
  * IPアドレスを表示するAPIを提供するサイト

---

## 実行結果の例

### プロキシ未使用

> {'ip': '\*\*\*.\*\*\*.\*\*\*.\*\*\*', 'hostname': 'p83d5cbf6.tokynt01.ap.so-net.ne.jp', 'city': 'Tokyo', 'region': 'Tokyo', 'country': 'JP', 'loc': '35.6892,139.6726', 'org': 'AS2527 Sony Network Communications Inc.', 'postal': '164-0013', 'timezone': 'Asia/Tokyo', 'readme': 'https://ipinfo.io/missingauth'}

### プロキシ使用

> {'ip': '185.230.163.237', 'hostname': '106d0201.cus13669.vps.st-srv.eu', 'city': 'Frankfurt am Main', 'region': 'Hesse', 'country': 'DE', 'loc': '50.1155,8.6842', 'org': 'AS48314 Michael Sebastian Schinzel trading as IP-Projects GmbH & Co. KG', 'postal': '60306', 'timezone': 'Europe/Berlin', 'readme': 'https://ipinfo.io/missingauth'}

---

## 依存関係エラーの対応方法

> requests.exceptions.InvalidSchema: Missing dependencies for SOCKS support.

* 上記のエラーはrequestsライブラリがSOCKSプロキシのサポートに必要な依存関係を満たしていない場合に発生する
* 解決策の一つとしてrequestsライブラリにSOCKSサポートを追加するパッケージをインストールする

### 対応手順

1. **requests** と **requests[socks]** パッケージをアンインストールする

    ```bash
    pip uninstall requests requests[socks]
    ```

2. **requests**、 **requests[socks]**、 **PySocks** パッケージを再インストールする

    ```bash
    pip install requests requests[socks] PySocks
    ```

    * PySocksはSOCKSプロキシのサポートを提供するための補助パッケージ