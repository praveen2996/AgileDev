from flask import Flask, request
from fileinput import filename
from flask import * 
import pandas as pd


app = Flask(__name__)


@app.route('/index')
def home():
    return "Hello, Flask!"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save("path/to/save/file")
    return "File uploaded successfully."

@app.route('/')  
def main():  
    return render_template("index.html")  
  
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        fileData = pd.read_csv(f)
        return render_template("Ack.html", name = f.filename, data = fileData)  

