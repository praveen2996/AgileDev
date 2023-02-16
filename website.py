from flask import Flask, request
from fileinput import filename
from flask import * 
from flask import Flask, request, redirect, url_for, render_template
import pandas as pd


app = Flask(__name__)
app.secret_key = 'my-secret-key'



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
  
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        dataset_file = request.files['file-dataset']
        rules_file = request.files['file-rules']
        dataset = pd.read_csv(dataset_file)
        column_names = list(dataset.columns)

        # Do something with dataset_file and rules_file here
         # Store the column names in a session
        session['column_names'] = column_names

        return redirect(url_for('success_message', message='Files uploaded and processed successfully!'))
    else:
        return redirect(url_for('home'))

@app.route('/success_message/<message>')
def success_message(message):
    column_names = session.get('column_names', [])

    return render_template('success.html', message=message, column_names=column_names)