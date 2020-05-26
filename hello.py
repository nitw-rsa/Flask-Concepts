from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route('/')
def home():
	return 'Rishabh Sharma'

@app.route('/about')
def about():
	return 'Engineer@'