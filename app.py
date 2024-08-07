import os
from model import model
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from Dataloader import loader
import logging

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = './files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods= ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
        
        # Getting data from form
        desc = request.form.get('ProjectDes')
        PandD = request.form.get('PandG')
        if PandD == '':
            PandD = 'Use Basic principal and guidlines of coding'
        # Correcting file path
        filepath = filepath.replace(os.sep, '/')
        print(filepath)
        if desc and filepath:
            try:
                response = model(filepath,desc,PandD)
                print(response)
                output = response
            except Exception as e:
                logging.error(f"Error found : {e}")

        return f"{output}"    

if __name__ == '__main__':
    app.run(debug=True)