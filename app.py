from flask import Flask, request
from flask_restful import Api
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def input_form():
      if request.method == 'POST':
          job_title = request.form['job_title']
          job_desc = request.form['job_desc']
          work_exp = request.form['work_exp']
      return render_template('index.html', title = job_title, desc = job_desc, exp = work_exp)

if __name__ == "__main__":
    app.run()
    app.debug = True
