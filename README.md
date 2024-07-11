# jwt-decode-sample
Flask フレームワークを使用して構築した API サーバーのサンプルです。`/api/protected` というエンドポイントに対し、JWT を使用してユーザーの認証を行います。

## 利用方法
1. `python main.py` なり Visual Studio Code のデバッガーなりで API サーバーを起動します。
1. [jwt.io](https://github.com/yus04/jwt-decode-sample.git) にて、任意の jwt トークンを生成します。
1. 生成したトークンを利用し、以下のコマンドをターミナルから実行します。
```
curl -H "Authorization: Bearer <jwt token>" http://127.0.0.1:5000/api/protected
```

