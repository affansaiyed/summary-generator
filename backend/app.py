from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import PyPDF2

app = Flask(__name__)
api = Api(app)

class Resume(FlaskForm):
    resume = FileField("resume")
    submit = SubmitField("submit")

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])

def home():
    form = Resume()
    return render_template('index.html', form = form)

def get_coverletter(text):
    return

if __name__ == "__main__":
    app.run(debug = True)

api.add_resource(Resume, "/resume/")