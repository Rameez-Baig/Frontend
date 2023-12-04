from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('course.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/sign')
# def signin():
#     if request.method == 'POST':
        
#         email = request.form['email']
#         password = request.form['password']
        
#         if email == 'user@example.com' and password == 'password123':
            
#             return redirect(url_for('welcome'))
#         else:
            
#             error_message = "Invalid email or password. Please try again."
#             return render_template('signin.html', error_message=error_message)
        
#     return render_template('signin.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/newbatches')
def basic():
    return render_template('newbatches.html')

@app.route('/machine')
def mac():
    return render_template('machine.html')


@app.route('/placements')
def place():
    return render_template('placements.html')

# @app.route('/webd')
# def web():
#     return render_template('webd.html')

# @app.route('/cloud')
# def cloud():
#     return render_template('cloud.html')
if __name__ == '__main__':
    app.run(debug=True)
