from flask import Flask, request
import requests
from flask import Flask, render_template
import os
from urllib.parse import unquote

app = Flask(__name__)
API_URL = "https://api-inference.huggingface.co/models/TuningAI/Llama2_7B_Cover_letter_generator"
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

'''class User:
     def __init__(self, job, description, experience, company):
          self.job = job
          self.description = description
          self.experience = experience
          self.company = company
          return
     
     def __str__(self):
          return f'Job Title: {self.job}, Preferred Qualifications: {self.description}, Hiring Company: {self.company}, Past Work Experience: {self.experience}'''

@app.route('/')
def home():
     return '''render_template('index.html')'''

@app.route('/submit', methods = ['POST'])
def predict():
      '''if request.method == 'POST':
          comp_name = request.form['comp_name']
          job_title = request.form['job_title']
          job_desc = request.form['job_desc']
          work_exp = request.form['work_exp']
          user = User(comp_name, job_title, job_desc, work_exp)
          if user is not None:
          response = requests.post(API_URL, headers=headers, json={'inputs': str(user)})
          if response.status_code == 200:
               processed_output = response.json()
          else:
               processed_output = "Error processing input"
      return processed_output #render_template('index.html', comp = comp_name, title = job_title, desc = job_desc, exp = work_exp, output = processed_output)'''
      reqData = unquote(request.form.get('info'))
      inputData = {"inputs": reqData}
      response = requests.post(API_URL, headers = headers, json = inputData)
      return response.json()

if __name__ == "__main__":
    app.run()
    app.debug = True
