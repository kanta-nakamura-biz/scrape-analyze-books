# scrape-analyze-books

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 概要

このリポジトリは、オンラインの書籍カタログサイト [Books to Scrape](http://books.toscrape.com/) から書籍に関するデータを自動的に収集し、収集したデータを分析して洞察を得るための Python スクリプトを含んでいます。

**主な目的:**

* ウェブスクレイピングの基本的な手法の実践
* 収集したデータを用いたデータ分析と可視化

## 含まれるスクリプト

* **`scrape_books.py`**: Books to Scrape から書籍のタイトル、製品ページのURL、価格、星評価、カテゴリなどの情報を抽出し、`books_data.csv` ファイルに保存します。接続エラー時の再試行処理と、サーバーへの負荷を考慮したアクセス間隔の設定が含まれています。
* **`analyze_books.py`**: `books_data.csv` を読み込み、以下の分析を行い、結果を画像ファイルとして保存します。
    * カテゴリ別の価格分布の可視化 (`price_by_category.png`)
    * 価格と星評価の相関関係の可視化 (`price_vs_rating.png`)
    * 価格と星評価の相関係数の算出と表示

## 実行方法

1.  このリポジトリをクローンまたはダウンロードします。
    ```bash
    git clone [https://github.com/YourUsername/scrape-analyze-books.git](https://github.com/YourUsername/scrape-analyze-books.git)
    cd scrape-analyze-books
    ```

2.  Python 3 がインストールされていることを確認してください。

3.  仮想環境を作成し、必要なライブラリをインストールします。
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS および Linux
    venv\Scripts\activate.bat  # Windows
    pip install -r requirements.txt
    ```

4.  `scrape_books.py` を実行してデータを収集します。
    ```bash
    python scrape_books.py
    ```
    スクレイピングされたデータは `books_data.csv` に保存されます。

5.  データ収集後、`analyze_books.py` を実行してデータの分析とグラフの生成を行います。
    ```bash
    python analyze_books.py
    ```
    分析結果のグラフは、`price_by_category.png` と `price_vs_rating.png` として保存されます。

## 分析内容

このプロジェクトでは、主に以下の分析を行っています。

* **カテゴリ別の価格分析**: 各書籍カテゴリの価格分布を箱ひげ図で可視化し、比較します。
* **価格と星評価の相関分析**: 書籍の価格とユーザー評価の間にどのような関係があるかを散布図で示し、相関係数を算出します。

## 注意事項

* このスクリプトは、ウェブサイトの構造が変更された場合、正常に動作しなくなる可能性があります。
* ウェブサイトへのアクセス頻度を適切に保つように設計されていますが、サーバーへの過度な負荷を避けるため、実行間隔を短くしすぎないようにしてください。
* `robots.txt` を確認し、スクレイピングが許可されているかを確認してください。

## ライセンス

このプロジェクトは MIT License の下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 今後の展望

* より高度なデータ分析手法の導入
* 自然言語処理を用いた書籍の説明文の分析
* 定期的なデータ更新の自動化

## 作者

Kanta Nakamura (https://github.com/kanta-nakamura-biz)