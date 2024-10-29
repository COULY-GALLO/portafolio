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



@app.route('/perfil')
def perfil():
    
        return render_template('perfil.html')

@app.route('/log_in')
def log_in():
    
        return render_template('log_in.html')











if __name__ == '__main__':
    app.run(debug=True, port=3500)
