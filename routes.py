from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm
import sys
import logging

app = Flask(__name__)
# import sys and logging and the following two lines added as per http://stackoverflow.com/questions/27882479/flask-projects-on-heroku-returns-500-internal-server-error

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask' ->NGL - Changed to below because of the error: "Flask sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL: role does not exist"
# Solution source: "http://www.bogotobogo.com/python/Flask/Python_Flask_App_0_Word_Count_Errors_Fixes.php"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/learningflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #->Save resources use
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index.html")
	
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    form = SignupForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form = form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            
            session['email'] = newuser.email
            return redirect(url_for('home'))
			
    elif request.method == 'GET':
        return render_template('signup.html', form = form)

@app.route("/home")
def home():
    return render_template("home.html")
	
if __name__ == "__main__":
    app.run(debug=True)
