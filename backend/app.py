from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
import PyPDF2
import torch
from transformers import AutoTokenizer, T5Model
import sentencepiece
import os
import re

app = Flask(__name__)
api = Api(app)

class Resume(FlaskForm):
    resume = FileField('Upload PDF', validators=[FileRequired()])
    submit = SubmitField('Submit')

@app.route('/')
@app.route('/home/', methods = ['GET', 'POST'])

def home():
        form = Resume()
        return render_template('index.html', form = form)

class ResumeInput(Resource):
    def __init__(self, text, summary):
        self.text = text
        self.summary = summary
        return

    def upload_file(self):
        if request.method =='POST':
            file = request.files.get('file')
            if file:
                pdf_text = self.parse_pdf(file)
        return pdf_text

    def parse_pdf(self, file):
        text = ''
        with open(file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(reader.numPages):
                page = reader.getPage(i)
                text = text + page.extract_text()
        text = re.sub(r"\b(\d{3})[-.]?(\d{3})[-.]?(\d{4})\b", "", text) # Removes Phone Number
        text = re.sub(r"\b(\d{10})\b", "", text) # Removes Phone Number P2
        text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "", text) # Removes Email
        text = re.sub("http[s]?\://\S+","",text) # Removes Links
        text = re.sub(r"(\r)|(\n)", text) # Removes escape characters
        return text
    
    def summarize(self, text):
        tokenizer = AutoTokenizer.from_pretrained("t5-base")
        model = T5Model.from_pretrained("t5-base")
        text = text

        input = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
        output = model.generate(input, max_length=250, min_length = 100, length_penalty = 5, num_beams = 2)
        summary = tokenizer.decode(output)

        return summary

    def get_coverletter(self, text):
        summary = self.summarize(text)
        return

    def get_linkedin_summary(self, text):
        summary = self.summarize(text)
        return

    
    def apply_template(self, text):
        return

if __name__ == "__main__":
    app.run(debug = True)

api.add_resource(ResumeInput, "/resume/")