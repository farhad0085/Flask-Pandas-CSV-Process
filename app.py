from flask import Flask, render_template, request, jsonify, url_for, redirect
import io, os
from NLG import csv_processing

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        
        files = request.files

        csv_1 = files['file_1']
        csv_2 = files['file_2']
        csv_3 = files['file_3']

        print(csv_1.filename)
        print(csv_2.filename)
        print(csv_3.filename)

        if csv_1.filename == "" or csv_2.filename == "" or csv_3.filename == "":
        	return jsonify({"message": "Something is wrong"}), 401

        #print(csv_3.read())
        #time.sleep(1)

        csv_1 = io.BytesIO(csv_1.read())
        csv_2 = io.BytesIO(csv_2.read())
        csv_3 = io.BytesIO(csv_3.read())

        try:
        	output_csv_1, output_csv_2 = csv_processing(csv_1, csv_2, csv_3)
        	output_csv_1.to_csv(os.path.join(app.root_path, 'static/csv', "NLGdata.csv"))
        	output_csv_2.to_csv(os.path.join(app.root_path, 'static/csv', "Chartsdata.csv"))
        except:
        	return jsonify({"message" : "error"}), 401

        filenames = ["NLGdata.csv", "Chartsdata.csv"]
        filelinks = [url_for('static', filename='csv/NLGdata.csv'), url_for('static', filename='csv/Chartsdata.csv'),]
        filesize = ["20 MB", "25 MB"]

        return jsonify({"filenames": filenames, "filesize": filesize, "filelinks": filelinks}), 200

    return render_template("index.html", title="Home"), 200