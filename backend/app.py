from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import PyPDF2
import torch
from transformers import AutoTokenizer, T5Model
import sentencepiece
import os

app = Flask(__name__)
api = Api(app)
ALLOWED_EXTENSIONS = {'pdf'}

class Resume(FlaskForm):
    resume = FileField("resume")
    submit = SubmitField("submit")

@app.route('/')
@app.route('/home/', methods = ['GET', 'POST'])

def home():
        form = Resume()
        return render_template('index.html', form = form)

class ResumeInput:
    def __init__(self, text, summary):
        self.text = text
        self.summary = summary
        return

    def upload_file(self):
        if request.method =='POST':
            file = request.files.get('file')
            if file:
                pdf_text = self.parse_pdf(file)
        return jsonify({'text': pdf_text})

    def parse_pdf(self, file):
        text = ''
        with open(file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(reader.numPages):
                page = reader.getPage(i)
                text = text + page.extract_text()
        return text

    def get_coverletter(self, summary):
        return

    def get_linked_summary(self, summary):
        return

    def summarize(self, text):
        tokenizer = AutoTokenizer.from_pretrained("t5-base")
        model = T5Model.from_pretrained("t5-base")
        text = text

        input = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
        output = model.generate(input, max_length=250, min_length = 100, length_penalty = 5, num_beams = 2)
        summary = tokenizer.decode(output)
        return summary

if __name__ == "__main__":
    app.run(debug = True)

api.add_resource(Resume, "/resume/")