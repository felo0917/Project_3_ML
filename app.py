import base64
import numpy as np
import io
from PIL import Image
import keras 
from keras import backend as k 
from keras.models import Sequential 
from keras.models import load_model 
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request,render_template
from flask import jsonify 
from flask import Flask 


app = Flask(__name__)

def get_model():
    global model
    model = load_model('Static/model/keras_cifar10_trained_model.h5')

    print(" *  Model loaded!")

def preprocess_image(image, target_size):
    if image.mode !="RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image 

print(" * Loading keras model...")
get_model()

@app.route("/")
def home():
    return render_template("predict.html")

@app.route("/predict" , methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size= (224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction':  {
            'Eczema': prediction[0][0],
            'Vascular_Tumors': prediction[0][1],
            'Bullous_Disease': prediction[0][2],
            'Nail_Fungus': prediction[0][3]
        }
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)

