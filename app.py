from flask import Flask, render_template, request,  url_for, redirect, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/clinical'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['WHOOSH_BASE'] = 'whoosh'

db = SQLAlchemy(app)


class Cancer(db.Model):
    rank = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    disease = db.Column(db.String(100))
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    conditions = db.Column(db.String(50))
    intervention = db.Column(db.String(50))
    locations = db.Column(db.String(200))

class AIDS(db.Model):
    rank = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    disease = db.Column(db.String(100))
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    conditions = db.Column(db.String(50))
    intervention = db.Column(db.String(50))
    locations = db.Column(db.String(200))

class Dengu(db.Model):
    rank = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    disease = db.Column(db.String(100))
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    conditions = db.Column(db.String(50))
    intervention = db.Column(db.String(50))
    locations = db.Column(db.String(200))

class Diabetes(db.Model):
    rank = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    disease = db.Column(db.String(100))
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    conditions = db.Column(db.String(50))
    intervention = db.Column(db.String(50))
    locations = db.Column(db.String(200))




#MySQL Configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='clinical'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql=MySQL(app)
#mysql.init_app(app)



@app.route('/')
def hello_world():
    return render_template('index.html')



#Home Page Without user

@app.route('/home')
def home():
    return render_template('index.html')





# Contact Us Page

@app.route('/contact')
def contact():
    return render_template('contact.html')





# After Login Home page

@app.route('/userhome', methods=['GET','POST'])
def userhome():
    return render_template('Afterlogin.html')




# About Route
@app.route('/about')
def about():
    return render_template('about.html')




# Log-out Route

@app.route('/logout')
def logout():
    return redirect(url_for('home'))






@app.route('/submit', methods=['GET','POST'])
def submit():
    return render_template('Submit.html')







# Cancer Data Table

@app.route('/cancertable', methods=['GET','POST'])
def cancertable():
    posts = Cancer.query.all()

    return render_template('Sample.html', posts = posts)


@app.route('/aidstable', methods=['GET','POST'])
def aidstable():
    posts = AIDS.query.all()

    return render_template('Sample.html', posts = posts)


@app.route('/dengutable', methods=['GET','POST'])
def dengutable():
    posts = Dengu.query.all()

    return render_template('Sample.html', posts = posts)



@app.route('/diabetestable', methods=['GET','POST'])
def diabetestable():
    posts = Diabetes.query.all()

    return render_template('Sample.html', posts = posts)




# Cancer Input

@app.route('/cancer', methods=['GET','POST'])
def cancer():
    if request.method == 'POST':
        disease = request.form['inputDisease']
        title = request.form['inputTitle']
        status = request.form['inputStatus']
        conditions = request.form['inputCondition']
        intervention = request.form['inputIntervention']
        locations = request.form['inputLocation']


        if title and status and conditions and intervention and locations:

            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO cancer(disease,title,status,conditions,intervention,locations) VALUES(%s, %s, %s, %s, %s, %s)", (disease,title,status,conditions,intervention,locations))
            # data = Cancer(title=request.form['inputTitle'], status = request.form['inputStatus'], conditions = request.form['inputCondition'], intervention=request.form['inputIntervention'], locations=request.form['inputLocation'])
            # db.session.add(data)
            # db.session.commit()


            mysql.connection.commit()


            cur.close()


        return redirect(url_for('userhome'))

    return render_template('SubmitForm.html')




#AIDS table input

@app.route('/aids', methods=['GET','POST'])
def aids():
    if request.method == 'POST':
        disease = request.form['inputDisease']
        title = request.form['inputTitle']
        status = request.form['inputStatus']
        conditions = request.form['inputCondition']
        intervention = request.form['inputIntervention']
        locations = request.form['inputLocation']


        if title and status and conditions and intervention and locations:

            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO aids(disease,title,status,conditions,intervention,locations) VALUES(%s, %s, %s, %s, %s, %s)", (disease,title,status,conditions,intervention,locations))
            # data = Cancer(title=request.form['inputTitle'], status = request.form['inputStatus'], conditions = request.form['inputCondition'], intervention=request.form['inputIntervention'], locations=request.form['inputLocation'])
            # db.session.add(data)
            # db.session.commit()


            mysql.connection.commit()


            cur.close()


        return redirect(url_for('userhome'))

    return render_template('SubmitForm.html')


# Dengu Table input

@app.route('/dengu', methods=['GET','POST'])
def dengu():
    if request.method == 'POST':
        disease = request.form['inputDisease']
        title = request.form['inputTitle']
        status = request.form['inputStatus']
        conditions = request.form['inputCondition']
        intervention = request.form['inputIntervention']
        locations = request.form['inputLocation']


        if title and status and conditions and intervention and locations:

            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO dengu(disease,title,status,conditions,intervention,locations) VALUES(%s, %s, %s, %s, %s, %s)", (disease,title,status,conditions,intervention,locations))
            # data = Cancer(title=request.form['inputTitle'], status = request.form['inputStatus'], conditions = request.form['inputCondition'], intervention=request.form['inputIntervention'], locations=request.form['inputLocation'])
            # db.session.add(data)
            # db.session.commit()


            mysql.connection.commit()


            cur.close()


        return redirect(url_for('userhome'))

    return render_template('SubmitForm.html')





# Diabetes table input

@app.route('/diabetes', methods=['GET','POST'])
def diabetes():
    if request.method == 'POST':
        disease = request.form['inputDisease']
        title = request.form['inputTitle']
        status = request.form['inputStatus']
        conditions = request.form['inputCondition']
        intervention = request.form['inputIntervention']
        locations = request.form['inputLocation']


        if title and status and conditions and intervention and locations:

            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO diabetes(disease,title,status,conditions,intervention,locations) VALUES(%s, %s, %s, %s, %s, %s)", (disease,title,status,conditions,intervention,locations))
            # data = Cancer(title=request.form['inputTitle'], status = request.form['inputStatus'], conditions = request.form['inputCondition'], intervention=request.form['inputIntervention'], locations=request.form['inputLocation'])
            # db.session.add(data)
            # db.session.commit()


            mysql.connection.commit()


            cur.close()


        return redirect(url_for('userhome'))

    return render_template('SubmitForm.html')






# Sign-up Route
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['inputFirstName']
        lastname = request.form['inputLastName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        _hashed_password = generate_password_hash(password)
        if firstname and lastname and email and password:
            #Create Cursor
            cur = mysql.connection.cursor()

            #Execute Query
            cur.execute("INSERT INTO users(f_name,l_name,email,password) VALUES(%s, %s, %s, %s)", (firstname,lastname,email,_hashed_password))


            # Commit to Database
            mysql.connection.commit()

            #Close Connection
            cur.close()

            return redirect(url_for('login'))

    return render_template('Register.html')



# LOGIN

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT email FROM users WHERE email = %s", [email])
        u_password = cur.execute("SELECT password FROM users WHERE email = %s", [email])
        if result > 0:
            # data = cur.fetchone()
            # d_password = data['PASSWORD']
            if check_password_hash(u_password,password) and email == result:
                session['logged_in'] = True
                session['email'] = email
                # name = cur.execute("SELECT f_name FROM users WHERE email = %s", [email])

                return redirect(url_for('userhome'))
                # return render_template('Afterlogin.html', name = name)
            else:
                #error = 'Invalid Login'
                render_template('Log.html')

            cur.close()
        else:
            #error = 'Email Id not found'
            return render_template('Log.html')
    return render_template('Log.html')

"""@app.route('/signUp', methods=['POST','GET'])
def signUp():
    try:
        # READ THE INPUT VALUE FROM HTML PAGE
        _firstname = request.form['inputFirstName']
        _lastname = request.form['inputLastName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _confirmpassword = request.form['inputConfirmPassword']

        # VALIDATE ALL INFORMATION ARE RECEIVED THROUGH INPUT
        if _firstname and _lastname and _email and _password and _confirmpassword:
            #conn = mysql.connect()
            #cursor = conn.cursor()
            cur = mysql.connection.cursor()
            _hashed_password = generate_password_hash(_password)
            cur.execute("INSERT INTO users(f_name,l_name,email,u_password) VALUES(%s,%s,%s,%s)", (_firstname,_lastname,_email,_password))
            cursor.execute(query,(_firstname,_lastname,_email,_password))
            #cursor.callproc('sp_createusers',(_firstname,_lastname,_email,_hashed_password))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User Created!!!'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(data[e])})
    finally:
        cursor.close()
        conn.close()"""

if __name__ == '__main__':
    app.run(debug=True)