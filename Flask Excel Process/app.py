from flask import Flask, render_template, request, jsonify
import os
from NLG import csv_processing

app = Flask(__name__)

upload_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        files = request.files

        file_1 = files['file_1']
        if file_1.filename != '':
            uploaded_path = os.path.join(upload_path, file_1.filename)
            file_1.save(uploaded_path)
            try:
                df = csv_processing(uploaded_path)
            except:
                return {}, 500
            response_back = df.to_dict()

            response_length = len(response_back['Open Ended Questions'])

            print(response_back)
            return jsonify(response_back, response_length)

    return render_template('index.html')


 