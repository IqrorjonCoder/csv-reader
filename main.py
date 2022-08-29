from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import os


app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')


@app.route("/")
def main():
    return render_template("main.html")



@app.route('/table', methods=['POST'])
def about_page():
    file = request.files['csv_file_input']
    file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(file_path)
    items = pd.read_csv(file_path).reset_index()
    return render_template("table.html", items=items)

