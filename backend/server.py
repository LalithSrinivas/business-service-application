from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
# CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/hello')
def say_hello_world():
    return {'result': "Hello World"}

@app.route('/api/hola', methods=['GET', 'POST'])
def say_hola_world():
    if request.method == 'POST':
        formState = json.loads(request.data)
        print('The form value for alignment is', formState['alignment'])
        return {'result': "Hola World"}

# FLASK_APP=server.py flask run


