from flask import Flask
import flask
from flask import request;
import joblib
import re
import urllib.request
app = Flask(__name__)

@app.route('/')
def main_page():
   return flask.render_template("index.html")

@app.route('/submit_email', methods=['GET', 'POST'])
def submit_eamil():
	print(request.form['email'])
	return classify_email(request.form['email'])

model_file_url="https://emailclassifiermodel6301.s3.us-east-2.amazonaws.com/CountVectorizer_Logistic_Regression_model.pkl"
model_file = urllib.request.urlopen(model_file_url)
model = joblib.load(model_file)
##from Validate_Input_Emails.ipynb by vharika333
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

##from Validate_Input_Emails.ipynb by vharika333
def classify_email(input_email):
	processed_email = preprocess_text(input_email)
	# Predict using the loaded model
	prediction = model.predict([processed_email])[0]
	label = 'Spam' if prediction == 1 else 'Not Spam'
	return label




if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)