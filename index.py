# -*- coding: utf-8 -*-
 
import os
import csv

from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template
from bottle import static_file
 
# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

@route('/css/<filename>')
def server_css(filename):
    """ setting for css file """
    return static_file(filename, root=BASE_DIR+"/static/css")

@route('/js/<filename>')
def server_js(filename):
    """ setting for js file """
    return static_file(filename, root=BASE_DIR+"/static/js")

@route('/img/<filename>')
def server_img(filename):
    """ setting for img file """
    return static_file(filename, root=BASE_DIR+"/static/img")

@route('/font/<filename>')
def server_font(filename):
    """ setting for font file """
    return static_file(filename, root=BASE_DIR+"/static/fonts") 

@route('/top')
@route('/top/')
@route('/top/<username>')
def top(username="anonymous"):

    # 配列を渡すための準備
    fizzbuzz = []
    for i in range(1, 100):
 
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append(str(i) + ": fizzbuzz")
        elif i % 3 == 0:
            fizzbuzz.append(str(i) + ": fizz")
        elif i % 5 == 0:
            fizzbuzz.append(str(i) + ": buzz")
        else:
            fizzbuzz.append(str(i))

    # name に username の値を渡す。
    return template('top',name=username, fizzbuzz=fizzbuzz)

@route('/form/')
def form():

    # キャラクター一覧を格納する配列
    character_list = []
    # character.csvを展開する
    with open(BASE_DIR + "/character.csv", "r") as csv_file:

        # csvライブラリでcsvファイルを読み込む
        reader = csv.reader(csv_file)
        # csvのタイトル部分を飛ばす
        next(reader)

        # 読み込んだcsvを一行ずつ処理
        for row in reader:
            character_list.append(
                {
                "id": row[0],
                "name": row[1],
                "level": row[2]
                }
            )

    return template('form', character_list=character_list)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)

