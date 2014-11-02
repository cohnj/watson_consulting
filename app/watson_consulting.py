from flask import Flask, render_template, jsonify, request, Response
import json


app = Flask(__name__)

@app.route('/')	# maps '/' to index()
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
