from flask import Flask, render_template, jsonify, request, Response
import requests


app = Flask(__name__)
watsonUser = 'nwu_student11'
watsonPwd = 'zMxA1lVA'

@app.route('/')	# maps '/' to index()
def index():
	return render_template('index.html')
 
@app.route('/question', methods=['POST'])
def question():
    question = request.form['watsonQuestion']
    jsonData = {"question" : {"questionText": question }}
    response = requests.post("https://watson-wdc01.ihost.com/instance/504/WatsonApp/deepqa/v1/question/1337",auth=(watsonUser,watsonPwd),data=jsonData)
    return response.text
    

if __name__ == '__main__':
	app.run(debug=True)
