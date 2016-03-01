# list-pullrequest

指定した日付以降にマージされたプルリクエストのリストを出力します。

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

### 他
+ `-h`でヘルプ
+ `./list-pullrequest.py`でも実行可能
