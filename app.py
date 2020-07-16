from flask import Flask, render_template, request, jsonify, url_for, redirect
import time
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
        	return jsonify({"message": "Something is wrong"}), 403

        #print(csv_3.read())
        time.sleep(1)

        filenames = ["file1.csv", "file2.csv"]
        filelinks = ["http://file1.csv", "http://file2.csv"]
        filesize = ["20 MB", "25 MB"]

        return jsonify({"filenames": filenames, "filesize": filesize, "filelinks": filelinks}), 200

    return render_template("index.html", title="Home"), 200