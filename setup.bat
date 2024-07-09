@echo off
REM コマンドプロンプトの文字コードを設定
chcp 932 >nul

REM ユーザーにメールアドレスとパスワードの入力を求める
set /p NAI_USERNAME=NovelAIのユーザー名（メールアドレス）を入力してください: 
set /p NAI_PASSWORD=NovelAIのパスワードを入力してください: 

REM .envファイルの作成
echo NAI_USERNAME=%NAI_USERNAME% > .env
echo NAI_PASSWORD=%NAI_PASSWORD% >> .env

REM venv作成メッセージ
echo venvの作成中です

REM 仮想環境の作成
python -m venv venv

REM 仮想環境をアクティブ化
call venv\Scripts\activate

REM パッケージインストールメッセージ
echo 必要なパッケージをインストール中です

REM 必要なパッケージをインストール
pip install novelai-api==0.28.1 
pip install gradio==4.29.0 

REM 完了メッセージ
echo セットアップが完了しました。仮想環境が作成され、パッケージがインストールされ、.envファイルが設定されました。
pause