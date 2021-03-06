import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory
import numpy as np
from keras.preprocessing import image
from keras.models import load_model


app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['Eczema', 'Vascular Tumors', 'Bullous Disease', 'Nail Fungus']

new_model = load_model('Static/model/skin_train.h5')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)   
        new_model.summary()
        test_image = image.load_img('images\\'+filename,target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis =0)
        result = new_model.predict(test_image)
        result1 = result[0]
        for i in range(3):
    
            if result1[i] == 1.:
                break
        prediction = classes[i]

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("template.html",image_name=filename, text=prediction)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=False)
  