from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def some():
	return "Sanjeeva Kaki"
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
