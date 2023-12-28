from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import PyPDF2
from transformers import T5Tokenizer, T5Model
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
        
        tokenizer = T5Tokenizer.from_pretrained("t5-base")
        model = T5Model.from_pretrained("t5-base")

        input_ids = tokenizer(self).input_ids  # Batch size 1
        decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        # forward pass
        outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        last_hidden_states = outputs.last_hidden_state
        return

if __name__ == "__main__":
    app.run(debug = True)

api.add_resource(Resume, "/resume/")