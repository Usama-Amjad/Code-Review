from langchain_community.llms import Ollama
from flask import Flask, request, redirect, url_for, render_template
from model import model
import os

app = Flask(__name__)

# Set the upload folder
# UPLOAD_FOLDER = './files'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/ai',methods= ["GET","POST"])
def home():
    # Rendering index.html
    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == "POST":
        print('ai post called')

        # Getting data
        json_content=request.json
        desc = json_content.get("desc")
        file_path = json_content.get("file_path")
        principles = json_content.get("principles")

        # Giving values to model
        response = model(file_path,desc,principles)

        # Response into Object
        response_answer={"answer":response}

        # Returning response
        return response_answer


def start_app():
    app.run(host="0.0.0.0",port=8080,debug=True)

if __name__=='__main__':
    start_app()
    
