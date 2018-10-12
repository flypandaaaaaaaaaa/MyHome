from flask import Flask,render_template,redirect,url_for
import os

app=Flask(__name__)

app.config['SECRET_KEY']='abcdefg'

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shutdown',methods=['GET'])
def shutdown():
    os.system("shutdown -s -t 1")
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)