  
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
# import tensorflow
# from tensorflow import keras

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

MODEL_PATH = 'Static\model\keras_cifar10_trained_model.h5'

model = load_model(MODEL_PATH)
model._make_predict_function()

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    #preprocessing the image
    x = image.img_to_array(img)

    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('flask.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        #save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)

        pred_class = decode_predictions(preds, top=1)
        result = str(pred_class[0][0][1])
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
