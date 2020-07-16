from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        files = request.files
        csv_1 = files[0]
        csv_2 = files[1]
        csv_3 = files[2]

    return render_template("index.html")