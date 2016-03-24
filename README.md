# 概要

指定した日付以降にマージされたプルリクエストのリストを出力します。

# 使い方
### ブランチ指定なし
```
$ python list-pullrequest.py '2016-03-01 12:00:00'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 53606  100 53606    0     0  39162      0  0:00:01  0:00:01 --:--:-- 39157

2016-03-01 15:28:05 hoge-branch -> choco-branch
2016-03-01 13:40:17 poyoyo -> master
2016-03-01 13:33:42 hoyoyo -> master
```

### ブランチ指定あり
```
$ python list-pullrequest.py '2016-03-01 12:00:00' -b master
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 53606  100 53606    0     0  39149      0  0:00:01  0:00:01 --:--:-- 39185

2016-03-01 13:40:17 poyoyo -> master
2016-03-01 13:33:42 hoyoyo -> master
```

### 二段階認証を設定している場合
- Githubの[アクセストークンページ](https://github.com/settings/tokens)で"Generate new token"する
- `bin/config.py`に発行したトークンを記載する

```
api = {
    "user": "自分のGithubユーザ名 (例:chocolat0w0)",
    "token": "発行したトークン (例:qwertyuiopasdfghjklzxcvbnm)"
}
```

### 他
+ `-h`でヘルプ
+ `./list-pullrequest.py`でも実行可能
