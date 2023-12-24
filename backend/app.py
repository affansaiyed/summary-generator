from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import PyPDF2
import os

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Resume(FlaskForm):
    resume = FileField("resume")
    submit = SubmitField("submit")

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])

def home():
    form = Resume()
    return render_template('index.html', form = form)

def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            pdf_text = parse_pdf(file_path)
        os.remove(file)
    return jsonify({'text': pdf_text})

def parse_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            text = text + page.extract_text()
    return text

def get_coverletter(text):
    return

def get_summary(text):
    return

def summarize(text):
    return

if __name__ == "__main__":
    app.run(debug = True)

api.add_resource(Resume, "/resume/")