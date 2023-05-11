from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/register',methods=['POST'])
def register():
	name  = request.form['name']
	mail = request.form['mail']
	password  = request.form['password']
	context = {'name':name,'mail':mail,'password':password}
	return render_template('register.html',data=context)

@app.route('/login',methods=['POST'])
def login():
	name  = request.form['name']
	password  = request.form['password']
	context = {'name':name}
	return render_template('home.html',data=context)

if __name__=="__main__":
	app.run(debug=True)