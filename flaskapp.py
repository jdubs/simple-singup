from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
import smtplib

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/signup'
db = SQLAlchemy(app)

def init_db():
    db.create_all()

class User(db.Model):
    __tablename__ = 'signup'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    signupDate = db.Column(db.DateTime, default=datetime.datetime.now)
    def __init__(self, email):
        self.email = email
	self.signupDate = datetime.datetime.now()

    def __repr__(self):
        return '<Email %r>' % self.email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup_entry():
    emailSignup = request.form['email']
    newUser = User(emailSignup)
    db.session.add(newUser)
    db.session.commit()
    flash("Thanks for sgining up!")
    sender = 'support@sportybird.io'
    receivers = ['support@sportybird.io']
    message = "New user signup: " + emailSignup
    blah = smtpObj = smtplib.SMTP('localhost')
    blah2 = smtpObj.sendmail(sender, receivers, message)
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run()
