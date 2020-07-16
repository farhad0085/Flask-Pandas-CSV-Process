from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        pass

    return render_template("index.html")