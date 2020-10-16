import os

from flask import Flask, render_template, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
# from flask import send_from_directory
from gevent.pywsgi import WSGIServer
from yourapplication import app
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

f

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



######## INITIATE FLASK APP #########################
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        get_image_class(user)
        return redirect(url_for('success', name=get_directory(user)))


@app.route('/success/<name>')
def success(name):
    return render_template('image_class.html')


# @app.route("/Skin")
# def graph():

#     return  render_template('Skin_index_copy.html')

if __name__ == '__main__':
    app.run(debug=True)
