import os
import numpy as np 
# Keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
# from keras.applications
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras import preprocessing
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# Define a flask app
app = Flask(__name__)
upload_folder = './Static/upload'
app.config['UPLOAD_FOLDER']=upload_folder
# Model saved with Keras model.save()
MODEL_PATH = 'Static\model\keras_cifar10_trained_model.h5'
# Load your trained model
model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')
# You can also use pretrained model from Keras
# Check https://keras.io/applications/


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    print(img)
    # Preprocessing the image
    x = image.img_to_array(img)
    print(x.shape)
    x = np.true_divide(x, 255)
    # x = np.expand_dims(x, axis=0)
    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    # x = preprocess_input(x, mode='caffe')
    preds = model.predict(x)
    preds=''
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    print('predict')
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['inputFile']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        # file_path = os.path.join(
        #     basepath, 'uploads', secure_filename(f.filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
        print(file_path)
        f.save(file_path)
        type_1 = preprocessing.image.load_img(file_path, target_size = (224, 224))
        input_arr = keras.preprocessing.image.img_to_array(type_1)
        input_arr = np.array([input_arr])  # Convert single image to a batch.
        # type_1_x = np.expand_dims(type_1, axis=0)
        # Make prediction
        preds = model_predict(input_arr, model)
        # Process your result for human
        pred_class = preds.argmax(axis=-1)            # Simple argmax
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        result = str(pred_class[0][0][1])               # Convert to string
        result = preds

        print(result)
        
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
