from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from model import model

app = Flask(__name__)


@app.route('/ai', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        print('AI POST called')

    desc = request.form.get("desc")
    file = request.files.get("file")
    file.filename = secure_filename(file.filename) + ".txt"
    principles = request.form.getlist("principles")

    if file:
        file_path = f"files/{file.filename}"
        file.save(file_path)

        response = model(file_path, desc, principles)

        response_answer = {"answer": response}

        return jsonify(response_answer)
    return jsonify("Model response error")


def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == '__main__':
    start_app()
