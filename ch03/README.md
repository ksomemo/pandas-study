# IPython

## 知らなかったこと
* printはIPython上でも整形されない
* モジュールに対するタブ補完
* var_name? による型情報などの表示(インストロペクション)
* 上記は関数に対しても可能である
* 上記の表示が長い場合、ページャーが使用される
* インストロペクションの対象には、\*などを使ってマッチングできる
* %paste によるクリップボードからの貼り付け
* %cpaste による何度も貼り付け可能なコピペモード
* %command をマジックコマンドという
* %quickref, %magic IPythonとマジックコマンドのヘルプがある
* GUIベースコンソールについては、qtconsoleを参照
* %logstart によるセッション中の入力コマンドをログに格納
    * このコマンド実行前からのコマンドもログに出力される
    * 結果の出力(out)はログに出力されない
* \!cmdの結果も変数に代入できる
* \!cmdでIPythonで作成した変数を使うには$var_nameとする
* %debug debugger(実際に困ったときに使ってみる)
* %time によるベンチマーク
* %timeit による複数回実行(自動)のベンチマーク
* %prun(%run -p)によるプロファイリング(ベンチマーク後の局所的に時間のかかる場所を調べるなど)
* browserによるIPythonの実行は、IPython HTML ノートブックという
* 上記は、`ipython notebook --pylab=inline` で実行する
* とても使いにくいが、別のサーバーで実行していれば使えるところが利点とのこと

## 疑問点
* run script.py と %run の違い
    * マジックコマンドの先頭の%は基本的には不要である
    * しかし、変数名とかぶった時はつける必要がある

## qtconsole

* QtというGUIベースのコンソールがある
* ipython qtconsole --pylab=inline として実行すると、図などをインライン表示できる

### 実行失敗
```
ipython qtconsole --pylab=inline
```

```
ImportError:
    Could not load requested Qt binding. Please ensure that
    PyQt4 >= 4.7 or PySide >= 1.0.3 is available,
    and only one is imported per session.
    Currently-imported Qt library:   None
    PyQt4 installed:                 False
    PySide >= 1.0.3 installed:       False
    Tried to load:                   ['pyside', 'pyqt']
```

### インストール

```
% brew install pyqt                                                                                                                 (git)-[master]
==> Installing dependencies for pyqt: qt, sip
==> Installing pyqt dependency: qt
```

```
ipython qtconsole --pylab=inline
ImportError: IPython.kernel.zmq requires pyzmq >= 2.1.11
```

### 確認(画像とグラフ)

qtconsoleを立ち上げたあとに下記を入力する

```
img = plt.imread('pydata-book/ch03/stinkbug.png')
imshow(img)
```

```
plot(randn(1000).cumsum())
```

* インライン表示されるので、閉じたりする必要がないので楽である
