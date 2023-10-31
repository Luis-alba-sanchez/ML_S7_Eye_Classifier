```markdown
# ML_S7_Eye_Classifier

ML_S7_Eye_Classifier is a web application that classifies eye images to determine if they are normal or show signs of a disease, and if so, it identifies the specific disease. This project was developed by Stephanie Li, Gabin Von Der Kalbusch, and Luis Aba Sanchez as part of a machine learning project at EFREI Paris.

## Usage

Before running the project, make sure to install the required dependencies listed in `requirements.txt`. To do this, open your terminal and navigate to the project directory. Then, execute the following commands:

```bash
pip install -r requirements.txt
python WebApp_eyeClassifier.py
```

## How It Works

The application employs a pre-trained deep learning model to classify eye images. Here's a brief overview of the process:

1. The user uploads an eye image via the web interface.
2. The image is processed and resized to a standard size of 224x224 pixels.
3. The image is normalized and converted to a format suitable for the model.
4. The model, loaded from `keras_model_2var.h5`, predicts the eye condition and returns a confidence score.
5. If the condition is detected as 'Risk,' a secondary model is used for a more specific classification.
6. The secondary model, loaded from `keras_model_all_var.h5`, provides a refined classification and confidence score.

## Model Details

- The primary model uses `keras_model_2var.h5` for binary classification of 'Normal' and 'Risk.'
- The secondary model, if needed, uses `keras_model_all_var.h5` for fine-grained disease classification.

The model classes are defined in `labels_2var.txt` and `labels_all_var.txt`.

## Running the Application

To run the application, execute the following command in your terminal:

```bash
python WebApp_eyeClassifier.py
```

The application will start, and you can access it by opening a web browser and navigating to `http://localhost:8000`.

## Authors

- Stephanie Li
- Gabin Von Der Kalbusch
- Luis Aba Sanchez

## License

This project is licensed under the MIT License. You can find more details in the `LICENSE` file.

## Acknowledgments

We would like to thank the EFREI Paris machine learning community for their support and guidance.
```

This updated README file provides a clearer and more detailed overview of your project, its usage, and how it works, making it easier for users to understand and use your application. It also includes sections for authors, licensing, and acknowledgments for additional context and transparency.
