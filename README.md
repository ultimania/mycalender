# mycalender
これは学習用のサンプルアプリです。
以下の手順に従って導入してください。

1. python等のソフトウェアをインストール
1. django等のライブラリをインストール
1. githubからリポジトリをクローン
1. ローカルでマイグレーション＆実行

### python等のソフトウェアをインストール

|ソフト|URL|
|---|---|
|python|https://www.python.org/downloads/|
|Sourcetree|https://www.sourcetreeapp.com/|


## django等のライブラリをインストール

Python導入後に
`python -m pip install django`
でdjangoを導入。

以降で必要なPythonライブラリは
`python -m pip install <パッケージ名>`
でインストールする。


## githubからリポジトリをクローン

Sourcetree導入後に
`git clone https://github.com/ultimania/mycalender.git`
でリポジトリをクローン。

カレントディレクトリにサンプルソースが展開されるので、以降はこれらのファイルを編集しながらアプリを作成する。


## ローカルでマイグレーション＆実行

ソースファイルの編集が完了したらベースディレクトリ（manage.pyがあるディレクトリ）で
`python manage.py makemigrations`
を実行。

正常にマイグレーションファイルが作成されたら
`python manage.py migrate`
でマイグレーション実行。

マイグレーションに成功したら
`python manage.py runserver 0.0.0.0:3000`
でアプリを起動。
あとはブラウザで`http://localhost:3000`にアクセスする。




