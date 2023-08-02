from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
# my db connection
local_server=True
app = Flask(__name__)
app.secret_key='SSH'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/stadiun seat booking'

db=SQLAlchemy(app)
#here we will db models i.e data tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
# here we will pas end points and run the function
@app.route("/")
def hello_world():
    
    
    
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/events")
def events():
    return render_template('events.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/signup")
def signup():
    return render_template('signup.html')
@app.route("/logout")
def logout():
    return render_template('logout.html')






    
@app.route("/test")
def t():
    try:
        Test.query.all()
        return 'My db is connected'
    except:
        return 'db not connected'
   
app.run(debug=True)