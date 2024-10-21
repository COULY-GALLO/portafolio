from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'patri'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ukc3pikk3fkkzvyi:E4W9DX4ZzG1t5NtFUIs7@beey6ofiqbnpaclvmjhy-mysql.services.clever-cloud.com:3306/beey6ofiqbnpaclvmjhy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
@app.route('/')
def home():
    
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=3500)
