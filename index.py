from flask import Flask,render_template,request,url_for,session,send_from_directory,redirect
import re
import ibm_db
app = Flask(__name__)

print("connecting...")

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rzm08887;PWD=NM02c9OExoYdTRH2;", "", "")
print("connected")

@app.route("/", methods=['POST', 'GET'])
def login():
	msg = ''
	if request.method == "POST":
		USERNAME = request.form["username" ]
		PASSWORD = request.form ["password" ]
		sq1 = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sq1)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			session['Loggedin'] = True
			session['USERID'] = account['USERID']
			session['USERNAME'] = account['USERNAME']
			msg = "logged in successfully"
			return redirect(url_for('home'))
		else:
			msg = "Incorrect Email/password"
	return render_template('login.html',msg=msg)


@app.route("/admin_login", methods=[ 'POST', 'GET'])
def admin_login():
	msg = ''
	if request.method == "POST":
		USERNAME = request. form[ "Username" ]
		PASSWORD = request. form[ "password"]
		sq1 = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sq1)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc (stmt)
		print (account)
		if account:
			session['Loggedin'] = True
			session['USERID'] = account ['USERID']
			session['USERNAME'] = account ['USERNAME']
			msg = "logged in successfully !"
			return redirect(url_for("home"))
		else:
			msg = "Incorrect Email/password"
			return render_template( 'admin_login.html', msg=msg)
	return render_template('admin_login.html', msg=msg)

@app.route("/agent_login", methods=[ 'POST', 'GET'])
def agent_login():
	msg = ''
	if request.method == "POST":
		USERNAME = request. form[ "Username" ]
		PASSWORD = request. form ["password"]
		sql = "SELECT * FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param (stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			session[ 'Loggedin'] = True
			session[ 'USERID'] = account [ 'USERID' ]
			session[ 'USERNAME' ] = account ["USERNAME" ]
			msg = "logged in successfully"
			return redirect(url_for('home'))
		else:
			msg = "Incorrect Email/password"
			return render_template('agent_login.html', msg=msg)
	return render_template('agent_login.html', msg=msg)


@app.route("/register",methods=['POST', 'GET'])
def register():
	msg = ''
	if request.method == "POST":
		USERNAME = request.form[ "username" ]
		EMAIL = request.form["email" ]
		PASSWORD = request.form["password" ]
		ROLE = 0
		sql = "SELECT * FROM USERN WHERE EMAIL=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, EMAIL)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template("signup.html")
		elif not re.match(r'[^@]+@[^@1+1. [^@]+',EMAIL):
			msg = "Invalid Email Address!"
		else:
			sql = "SELECT count(*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sq1 = "INSERT INTO USERN VALUES (?,?,?,?,?)"
			prep_stmt = ibm_db.prepare(conn, insert_sq1)
			ibm_db.bind_param(prep_stmt, 1, length['1']+1)
			ibm_db.bind_param(prep_stmt, 2, ROLE)
			ibm_db.bind_param(prep_stmt, USERNAME)
			ibm_db.bind_param(prep_stmt, EMAIL)
			ibm_db.bind_param(prep_stmt, 5, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered !"
	return render_template('login.htm1', msg=msg)


@app.route('/admin _register', methods=['POST', "GET"])
def admin_register():
	if request.method == "POST":
		USERNAME = request.form["Username" ]
		EMAIL = request.form["Email"]
		PASSWORD = request.form["password"]
		ROLE = request.form['role']
		secret_key = request.form["secret"]
		sql = "SELECT FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt, 2, PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			secret_key == "12345"
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template('signup.htm1')
		else:
			secret_key == "12345"
			sql="SELECT count (*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sq1 = "INSERT INTO USERN VALUES (?,?, ?, ?, ?)"
			prep_stmt = ibm_db.prepare(conn, insert_sq1)
			ibm_db.bind_param(prep_stmt, 1, length['1']+1)
			ibm_db.bind_param(prep_stmt, ROLE)
			ibm_db.bind_param(prep_stmt, 3, USERNAME)
			ibm_db.bind_param(prep_stmt, EMAIL)
			ibm_db.bind_param(prep_stmt, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered"
			return render_template( 'admin_login.html',msg=msg)
	return render_template('admin_register.html',msg=msg)


@app.route('/agent_register', methods=[' POST', 'GET'])
def agent_register():
	msg=''
	if request .method == 'POST':
		USERNAME = request.form[ "username" ]
		EMAIL = request.form["emai1"]
		PASSWORD = request.form[ "password" ]
		ROLE = request.form['role']
		secret_key = request.form["secret" ]
		sql = "SELECT FROM USERN WHERE USERNAME=? AND PASSWORD=?"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, USERNAME)
		ibm_db.bind_param(stmt,PASSWORD)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			secret_key = "12345"
			msg = "Your signup deatils are already exists in the database Please login"
			return render_template("signup.htm1")
		else:
			secret_key = "12345"
			sql = "SELECT count(*) FROM USERN"
			stmt = ibm_db.prepare(conn, sql)
			ibm_db.execute(stmt)
			length = ibm_db.fetch_assoc(stmt)
			print(length)
			insert_sql = "INSERT INTO USERN VALUES(?,?,?,?,?)"
			prep_stmt = ibm_db.prepare(conn, insert_sql)
			ibm_db.bind_param(prep_stmt, 1, length['1' ]+1)
			ibm_db.bind_param(prep_stmt, 2, ROLE)
			ibm_db.bind_param(prep_stmt, 3, USERNAME)
			ibm_db.bind_param(prep_stmt, 4, EMAIL)
			ibm_db.bind_param(prep_stmt, PASSWORD)
			ibm_db.execute(prep_stmt)
			msg = "You have successfully registered"
			return render_template('admin_login.html', msg=msg)
	return render_template("agent_register.html",msg=msg)


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('USERID', None)
	return render_template('indexold.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
	sql = "SELECT • FROM USERN WHERE USERID=?" + str(session['USERID'])
	stmt = ibm_db.prepare(conn,sql)
	ibm_db.prepare(conn, sql)
	ibm_db.execute(stmt)
	User = ibm_db.fetch_tuple(stmt)
	print(User)
	print("data fetched")
	if User[1] == '0':
		if request.method == "POST":
			f = request.files["image"]
			TITLE = request. form.get("title")
			DESCRIPTION = request.form.get("description")
			LAT = request. form.get("lat")
			LONG = request. form.get("lon")
			IMAGE_ID="0"
	if(LAT== "" and LONG == ""):
		return render_template('homeuser.html', data=0)
	else:
		sql = "SELECT * FROM USERN WHERE USERID = " +str(session['USERID'])
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		data = ibm_db. fetch_assoc(stmt)
		print (data)
		sq1 = "INSERT INTO TICKETS VALUES(?,?, NULL,?,?,NULL,?,?,?)"
		stmt1 = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt1, 1, data['USERID'])
		ibm_db.bind_param(stmt1, 2, data['USERNAME'])
		ibm_db.bind_param(stmt1, 3, TITLE)
		ibm_db.bind_param(stmt1, 4, DESCRIPTION)
		ibm_db.bind_param(stmt1, LAT)
		ibm_db.bind_param(stmt1, 6, LONG)
		ibm_db.bind_param(stmt1,IMAGE_ID)
		ibm_db.execute(stmt1)


if __name__=="__main__":
	app.run(debug=True)