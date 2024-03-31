from flask import Flask, request
import requests
from flask_restful import Api
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


app = Flask(__name__)
model_url = ''

class User:
     def __init__(self, job, description, experience, company):
          self.job = job
          self.description = description
          self.experience = experience
          self.company = company
          return
     
     def __str__(self):
          return f'Job Title: {self.job}, Preferred Qualifications: {self.description}, Hiring Company: {self.company}, Past Work Experience: {self.experience}'

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
          user = User(comp_name, job_title, job_desc, work_exp)
          response = requests.post(model_url, json={'inputs': str(user)})
          if response.status_code == 200:
               processed_output = response.json().get('processed_output')
          else:
               processed_output = "Error processing input"
      return render_template('index.html', comp = comp_name, title = job_title, desc = job_desc, exp = work_exp, output = processed_output)

@app.route('/output')
def get_output():
     
     return render_template('output.html')

if __name__ == "__main__":
    app.run()
    app.debug = True
