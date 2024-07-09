# NovelAI-Easy-Web-UI
## Windowsでのインストール方法

Python 3.10.7およびGitが必要です

セットアップには setup.bat を実行してください

またはターミナルで以下を実行してください
```powershell
git clone https://github.com/Tesixki/NovelAI-Easy-Web-UI
cd NovelAI-Easy-Web-UI

python -m venv venv
.\venv\Scripts\activate

pip install novelai-api==0.28.1
pip install gradio==4.29.0
```

## ログインIDとパスワードの記載された.envファイルを作成

このプログラムにはNovelAIのログインID(メールアドレス)とパスワードを記載した
.envファイルが必要です。

```powershell
NAI_USERNAME=mail@mail.com
NAI_PASSWORD=password
```

## 実行方法

start.bat を実行してください

またはターミナルで以下を実行してください
```powershell
.\venv\Scripts\activate
python main.py
```