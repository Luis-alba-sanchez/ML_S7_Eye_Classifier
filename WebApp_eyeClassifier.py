from flask import Flask, render_template, request
from keras.models import load_model
from PIL import ImageOps, Image
import numpy as np
import base64

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # ======================
    # ===== load image =====
    # ======================
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    image = Image.open(image_path).convert('RGB')
    
    # ==========================
    # ===== image treatment =====
    # ==========================
    # convert image to (224, 224)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    # convert image to numpy array
    image_array = np.asarray(image)
    # normalize image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # set model input
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # =====================
    # ===== the model =====
    # =====================
    # load classifier
    model = load_model('./model_2var/keras_model_2var.h5')
    # load the classes
    with open('./model_2var/labels_2var.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
        f.close()
    # make prediction
    prediction = model.predict(data)
    # get prediction
    index = np.argmax(prediction)
    # get prediction's class
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    classification = '%s (%.2f%%)' % (class_name, confidence_score*100)

    if class_name == 'Risk':
        # ============================
        # ===== the second model =====
        # ============================
        # load classifier
        model2 = load_model('./model_all_var/keras_model_all_var.h5')
        # load the classes
        with open('./model_all_var/labels_all_var.txt', 'r') as f:
            class_names2 = [a[:-1].split(' ')[1] for a in f.readlines()]
            f.close()
        # make prediction
        prediction2 = model2.predict(data)
        # get prediction
        index2 = np.argmax(prediction2)
        # get prediction's class
        class_name2 = class_names2[index2]
        confidence_score2 = prediction2[0][index2]

        classification2 = '%s (%.2f%%)' % (class_name2, confidence_score2*100)

        print(classification2)

        return render_template('index.html', prediction=classification, prediction2=classification2)

    return render_template('index.html', prediction=classification)

if __name__ == '__main__':
    app.run(port=3000,  debug=True)
