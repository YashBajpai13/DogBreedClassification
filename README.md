<h1>Dog Breed Classification Project</h1>
This project focuses on classifying dog breeds using the EfficientNetV2 B0 model. The model has been trained on a dataset comprising 120 different dog breeds, achieving an accuracy of approximately 84%. The deployment of this project is hosted on the Streamlit Community Cloud, allowing users to easily interact with the classification system.
<br>
<h2>Project Overview</h2>
<br>
1. Model Architecture
The core of this project is the EfficientNetV2 B0 model, a state-of-the-art convolutional neural network known for its efficiency and high performance in image classification tasks.
<br>
<br>
2. Dataset (Credits to Jessica Li (https://www.kaggle.com/jessicali9530))
The dataset can be found on kaggle (https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset), I have not included it in the repository. It is a comprehensive collection that enables the model to generalize well across various breeds.
<br>
<br>
3. Training
The training details can be found in the dogbreedclassification.ipynb notebook.
<br>
<br>
<h3>Deployment</h3>
The deployment of this dog breed classification project is hosted on the Streamlit Community Cloud, providing a user-friendly interface for breed prediction. Users can upload images of dogs, and the model will predict the most likely breed along with its confidence level.
<br>
<h3>Access the Deployment</h3>
To interact with the deployed model, simply visit the following link: https://dogbreed.streamlit.app/
<br>
<h3>Usage</h3>
Upload Image: On the web interface, users can upload an image of a dog for classification. Sample Images are provided in the "Sample Test Images" folder.
<br>
Prediction: Once the image is uploaded, the model processes it and predicts the most probable dog breed along with a confidence score.
<br>
Explore Results: Users can explore the predicted breed and confidence level, gaining insights into the model's classification.
<br>
<br>
<h3>To run this project locally, follow these steps:</h3>
<br>
<b>Clone the repository:</b>
git clone https://github.com/your-username/dog-breed-classification.git
<br>
<b>Install dependencies: </b>
pip install -r requirements.txt
<br>
<b>To run the streamlit app: </b>
streamlit run streamlit_app/app.py
Open the provided local URL in your web browser and start using the dog breed classification system.
<br>
<h4>Acknowledgments</h4>
Special thanks to the Streamlit Community Cloud for hosting the deployment.
EfficientNetV2 B0 implementation based on the EfficientNetV2 repository.
Feel free to explore, contribute, and provide feedback on this dog breed classification project!
<br>
