import markdown
import os
#Import the framework
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    """Present some documentation"""
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        #read the content of the file
        content = markdown_file.read()

        #Conver to HTMl
        return markdown.markdown(content)

class Analitycs(Resource):
    def get(self, doc):
        return{'message': 'Dummy', 'data': {'document': ''}}

#api.add_resource(Analitycs, '/doc/<strin:doc>')