import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import re

#st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Dog Breed Classifier")
@st.cache_resource()#allow_output_mutation=True)
def load_model():
    """
    Loads trained model
    """
    #model = tf.keras.models.load_model("effnet_saved_model")
    model = tf.keras.layers.TFSMLayer("effnet_saved_model", call_endpoint='serving_default')
    return model

model = load_model()

st.write("""
         This is a pretrained Efficient Net v2 B0 model trained on a dataset of 120 different dog breeds.
        """)

file = st.file_uploader("Upload an image of a dog, and the model will provide accurate breed predictions.", type = ['jpg', 'png'])

def predict(image, model):
    size = (224, 224)
    image = ImageOps.fit(image, size)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, :]
    prediction = model(img_reshape)
    return prediction


if file is None:
    st.text("Upload an image in jpg or png format")
else:
    image = Image.open(file)
    st.image(image, use_column_width = True)
    predictions = predict(image, model)
    class_names = ['Chihuahua', 'Japanese_spaniel', 'Maltese_dog', 'Pekinese', 'Shih-Tzu', 'Blenheim_spaniel', 'papillon', 'toy_terrier', 'Rhodesian_ridgeback',
 'Afghan_hound','basset', 'beagle', 'bloodhound', 'bluetick', 'black-and-tan_coonhound', 'Walker_hound', 'English_foxhound', 'redbone', 'borzoi',
 'Irish_wolfhound', 'Italian_greyhound', 'whippet', 'Ibizan_hound', 'Norwegian_elkhound', 'otterhound', 'Saluki', 'Scottish_deerhound', 'Weimaraner',
 'Staffordshire_bullterrier', 'American_Staffordshire_terrier', 'Bedlington_terrier', 'Border_terrier', 'Kerry_blue_terrier', 'Irish_terrier', 'Norfolk_terrier',
 'Norwich_terrier', 'Yorkshire_terrier', 'wire-haired_fox_terrier', 'Lakeland_terrier', 'Sealyham_terrier', 'Airedale', 'cairn', 'Australian_terrier',
 'Dandie_Dinmont', 'Boston_bull', 'miniature_schnauzer', 'giant_schnauzer', 'standard_schnauzer', 'Scotch_terrier', 'Tibetan_terrier', 'silky_terrier',
 'soft-coated_wheaten_terrier', 'West_Highland_white_terrier', 'Lhasa', 'flat-coated_retriever', 'curly-coated_retriever', 'golden_retriever', 'Labrador_retriever',
 'Chesapeake_Bay_retriever', 'German_short-haired_pointer', 'vizsla', 'English_setter', 'Irish_setter', 'Gordon_setter', 'Brittany_spaniel', 'clumber',
 'English_springer', 'Welsh_springer_spaniel', 'cocker_spaniel', 'Sussex_spaniel', 'Irish_water_spaniel', 'kuvasz', 'schipperke', 'groenendael',
 'malinois', 'briard', 'kelpie', 'komondor', 'Old_English_sheepdog', 'Shetland_sheepdog', 'collie', 'Border_collie', 'Bouvier_des_Flandres', 'Rottweiler',
 'German_shepherd', 'Doberman', 'miniature_pinscher', 'Greater_Swiss_Mountain_dog', 'Bernese_mountain_dog', 'Appenzeller', 'EntleBucher', 'boxer',
 'bull_mastiff', 'Tibetan_mastiff', 'French_bulldog', 'Great_Dane','Saint_Bernard', 'Eskimo_dog', 'malamute', 'Siberian_husky', 'affenpinscher',
 'basenji', 'pug', 'Leonberg', 'Newfoundland', 'Great_Pyrenees', 'Samoyed', 'Pomeranian', 'chow', 'keeshond', 'Brabancon_griffon', 'Pembroke', 'Cardigan',
 'toy_poodle', 'miniature_poodle', 'standard_poodle', 'Mexican_hairless', 'dingo', 'dhole', 'African_hunting_dog']

    #string = f"This image is of a {class_names[np.argmax(predictions)]} dog, confidence level : {np.max(predictions) * 100} %"
    string = f"This image is of a {class_names[np.argmax(tf.squeeze(predictions['OutputLayer']))]} dog, confidence level : {np.max(tf.squeeze(predictions['OutputLayer'])) * 100} %"
    st.success(string)