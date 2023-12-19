import pandas as pd
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
import PyPDF2

app = Flask(__name__)
api = Api(app)

class Resume(Resource):

    def get(self):
        return
    
    def post(self):
        return

api.add_resource(Resume, "/resume/")