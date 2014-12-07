from flask import Flask, render_template, jsonify, request, Response
import requests,json


app = Flask(__name__)
watsonUser = requests.auth.b64encode('nwu_student11')
watsonPwd = requests.auth.b64encode('zMxA1lVA')
watson_auth = requests.auth.b64encode('nwu_student11:zMxA1lVA')

@app.route('/')	# maps '/' to index()
def index():
	return render_template('index.html')
 
@app.route('/question', methods=['POST','GET'])
def question():
	question = request.args.get('watsonQuestion', "", type=str)
	#if request.form['watsonQuestion']:
	#	question = request.form['watsonQuestion']
	#else:
	#	question = "Who is a US citizen?"
	print question
	watson_headers= {"Accept":"application/json","Content-Type":"application/json","X-SyncTimeout":30,"Authorization":'Basic ' + watson_auth}	
	jsonData = json.dumps({"question" : {"questionText": question}})
	#jsonData = {"question" : {"questionText": question}}
	#response = requests.post("https://watson-wdc01.ihost.com/instance/504/deepqa/v1/question",auth=(watsonUser,watsonPwd),data=jsonData,headers=watson_headers)
	response = requests.post("https://watson-wdc01.ihost.com/instance/504/deepqa/v1/question",data=jsonData,headers=watson_headers)
	#print response.text
	response = response.json()
	print response['question']['evidencelist'][0]['text']
    
	bestAnswer = response['question']['evidencelist'][0]['text']

	return jsonify(result=bestAnswer)

if __name__ == '__main__':
	app.run(debug=True)
