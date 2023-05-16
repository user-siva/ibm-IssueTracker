from flask import Flask,render_template,request,url_for,session,send_from_directory,redirect
import ibm_db
app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb;HOSTHAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;UID=rzm08887;PWD=NM02c9OExoYdTRH2",'','')
print("connected")

@app. route("/login", methods=['POST', 'GET'])
def login():
	msg = ''
	if request .method == "POST":
		USERNAME = request.form["username" ]
		PASSWORD = request.form ["password" ]
		sq1 = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sq1)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print (account)
	if account:
		session['Loggedin'] = True
		session['USERID'] = account['USERID']
		session['USERNAME'] = account['USERNAME']
		msg = "logged in successfully"
		return redirect(url_for('home'))
	else:
		msg = "Incorrect Email/password"
	return render_template('login.html',msg=msg)


if __name__=="__main__":
	app.run(debug=True)