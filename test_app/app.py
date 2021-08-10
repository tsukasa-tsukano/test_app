from flask import Flask, render_template, session, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pandas as pd
import openpyxl

#インスタンスの作成
app = Flask(__name__)

#暗号鍵の作成
key = os.urandom(21)
app.secret_key = key

#メイン
@app.route("/")
def index():
    #表示させたいdataを渡す
    return render_template('index.html')

@app.route('/edit', methods=["POST"])
def edit():
    #取り出す
    day = request.form['day']
    print(day)

    return redirect(url_for('index'))
#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)