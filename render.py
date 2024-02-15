from flask import Flask, request, render_template
import datetime
from base64 import b64encode
import os
current = datetime.datetime.now()
try:
    ids = os.environ['USER']
    print(ids)
except KeyError:
    print("User is not Set")
    exit(1)

flag = b64encode(bytes(ids + "---" +"assign6"  +"---" + current.strftime("%Y-%m-%d %H:%M:%S"), 'utf-8')).decode('utf-8')


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/get_flag",methods=['POST','GET'])
def get_flag():
    return "hello"

@app.route("/home", methods=['POST'])
def home():
    xss = request.form['string']
    return render_template("index.html",xss = xss)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')