from flask import Flask,render_template,url_for,request
import speech_recognition as sr
from rasa.nlu.model import Interpreter


app = Flask(__name__)

interpreter = None 
def load_model():
	global interpreter 
	interpreter = Interpreter.load("../Rasa/models/nlu") #Unzip the model and write the path to that model

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/record')
def record():
	r = sr.Recognizer()
	with sr.Microphone() as source: 
		audio = r.listen(source, phrase_time_limit=10)
	try: 
		message = (r.recognize_google(audio))
	except sr.UnknownValueError:
		message = "Did not understand"
	
	rasa_data = interpreter.parse(message)
	my_prediction = ["intent: "+rasa_data['intent']['name']] + [rasa_data['entities'][i]['entity']+": "+rasa_data['entities'][i]['value'] for i in range(len(rasa_data['entities']))]

	return render_template('result.html', message = message, prediction = my_prediction)






if __name__ == '__main__':
	app.debug = True
	print("Loading model and flask starting server...")
	load_model() #Preloading the model 
	print("Model is loaded")
	app.run(debug=True)