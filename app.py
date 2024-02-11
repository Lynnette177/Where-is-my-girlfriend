from flask import Flask, render_template, request
import time
import subprocess
import os
from pushover import Client
client = Client("", api_token="")#pushover api

app = Flask(__name__)

def process_input(user_input):
    if user_input:
        return f"{user_input}"
    else:
        return "找不到宝宝了！"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        result = process_input(user_input)
        client.send_message(result, title="找不到宝宝了！")
        return render_template('index.html', result="已发送："+result)
    else:
        return render_template('index.html', result="默认发送：找不到宝宝了！")

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
