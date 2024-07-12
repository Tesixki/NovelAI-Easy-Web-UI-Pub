@echo off
REM コマンドプロンプトの文字コードを設定
chcp 932 >nul

@echo off
REM 仮想環境を有効化
call .\venv\Scripts\activate

REM main.pyを実行
python main.py

REM メッセージ
echo 起動しました