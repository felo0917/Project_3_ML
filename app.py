import os

from flask import Flask, render_template, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from gevent.pywsgi import WSGIServer
from yourapplication import app
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()


from get_prediction import get_prediction
from generate_html import generate_html
from torchvision import models
import json


######## INITIATE FLASK APP #########################
app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# put model stuff here

# define the function to get the images from the url and predicted the class
def get_image_class(path):
    # get images from the URL and store it in a given path
    get_images(path)
    # predict the image class of the images with provided directory
    path = get_path(path)
    images_with_tags = get_prediction(model, imagenet_class_mapping, path)
    # generate html file to render once we predict the classes
    generate_html(images_with_tags)

@# by deafult render the "home.html"    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        # if search button hit, call the function get_image_class 
        get_image_class(user)
        #render the image_class.html
        return redirect(url_for('success', name=get_directory(user)))


@app.route('/success/<name>')
def success(name):
    return render_template('image_class.html')


if __name__ == '__main__' :
    app.run(debug=True)