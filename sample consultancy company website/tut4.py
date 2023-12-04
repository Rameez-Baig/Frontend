from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contacts'
db = SQLAlchemy(app)

class Cont(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phno = db.Column(db.String(12), unique=True, nullable=False)
    Date = db.Column(db.String(120), nullable=True)

@app.route("/")
def hello():
    return render_template('ind5.html')

@app.route("/join")
def abt():
    return render_template('join.html')

@app.route("/cont", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        

        entry = Cont(name=name, email=email, phno=phone, Date = datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template('contac.html')

@app.route("/staffaugumentation")
def staff():
    return render_template('staff.html')

@app.route("/leadership")
def leadership():
    return render_template('leadership.html')

@app.route("/aboutus")
def about():
    return render_template('aboutus.html')

@app.route("/consulting")
def consult():
    return render_template('consulting.html')

@app.route("/softwaredevelopment")
def softdev():
    return render_template('softwaredevelopment.html')

@app.route("/coinpay")
def coin():
    return render_template('coinpay.html')

@app.route("/streamcast")
def stream():
    return render_template('stream.html')

@app.route("/privacypolicy")
def privacy():
    return render_template('privacy.html')

@app.route("/industries")
def industrie():
    return render_template('industries.html')

if __name__ == "__main__":
    app.run(debug=True)
