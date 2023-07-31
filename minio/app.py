from flask import Flask, render_template, request, jsonify
from colorama import Fore, Style
import python_minio

app = Flask(__name__)

@app.route("/", methods=["GET"])
def minio_console():
    return render_template("minio_console.html")

@app.route("/minio_action", methods=["POST"])
def minio_action():
    client_input = request.form["client_input"]
    result = python_minio.switch(client_input)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)