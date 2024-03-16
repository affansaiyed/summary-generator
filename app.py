from flask import Flask, request
from flask_restful import Api
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


app = Flask(__name__)

class User:
     def __init__(self, job, description, experience, company):
          self.job = job
          self.description = description
          self.experience = experience
          self.company = company
          return
     
     def __str__(self):
          return f'Job Title: {self.job}, Preferred Qualifications: {self.description}, Hiring Company: {self.company}, Past Work Experience: {self.experience}>'

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def index():
      if request.method == 'POST':
          comp_name = request.form['comp_name']
          job_title = request.form['job_title']
          job_desc = request.form['job_desc']
          work_exp = request.form['work_exp']
      return render_template('index.html', comp = comp_name, title = job_title, desc = job_desc, exp = work_exp)

if __name__ == "__main__":
    app.run()
    app.debug = True
