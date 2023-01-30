# JAPANESE ENGLISH BILINGAL CORPUS PARSER TO JSONL

元データ
https://www.kaggle.com/datasets/team-ai/japaneseenglish-bilingual-corpus?resource=download

上記データをjsonl形式に変換するパーサースクリプトです。以下の手順に従って、実行してください。

1. Kaggleからデータセットをダウンロード
2. このリポジトリをダウンロード
3. リポジトリに`dataset`ディレクトリを作成し`dataset`ディレクトリ内部でkaggleからダウンロードしたデータセットを解凍
4. `dataset/wiki_corpus_2.01`ディレクトリが作成されていることを確認する。
5. `$ python main.py`を実行

標準ライブラリのみで完結します。

## 構造

一行ごとにjsonが記載されています。各行は以下のような構成になっています。
```
{
    "ja": "こんにちは", #オリジナルの文章。日本語。
    "en-trans-v1": "Hello", # 日本語を母語とする翻訳者による翻訳文
    "en-trans-v2": "Hello", # 英語を母語とする翻訳者がv1をチェック・修正した翻訳文
    "en-check": "Hello", # 日本語を母語とする翻訳者が専門用語および専門分野の知識のチェック・修正をしたもの。
}
```

`en-trans-v1`は一次翻訳。`en-trans-v2`は二次翻訳。`en-check`は最終チェックに対応しています。詳細については、元データURLにてご確認ください。

## データ数

487507行。

## LICENCE

unlicence