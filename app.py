from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        
        files = request.files

        csv_1 = files['file_1']
        csv_2 = files['file_2']
        csv_3 = files['file_3']

        if csv_1.filename == "" or csv_2.filename == "" or csv_3.filename == "":
        	return jsonify({"message": "Something is wrong"}), 403

        #print(csv_3.read())

    return render_template("index.html", title="Home")

@app.route("/result")
def result():

    return render_template("result.html", title="Result")