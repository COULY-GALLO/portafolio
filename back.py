import plotly.graph_objects as go
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'patri'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ukc3pikk3fkkzvyi:E4W9DX4ZzG1t5NtFUIs7@beey6ofiqbnpaclvmjhy-mysql.services.clever-cloud.com:3306/beey6ofiqbnpaclvmjhy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
load_dotenv()
usuario = os.getenv("usuario")
contraseña = os.getenv("contraseña")


@app.route('/')
def home():
        
 language_data = {
        'labels': ['Python', 'JavaScript', 'HTML', 'CSS', 'Otros'],
        'percentages': [40, 30, 15, 10, 5]  # Cambia estos valores según tus necesidades
    }
    
   
 fig = go.Figure(data=[go.Pie(labels=language_data['labels'], values=language_data['percentages'], hole=0.3)])
    
    # Convertir el gráfico a HTML
 graph_html = fig.to_html(full_html=False)

    
 return render_template('home.html', graph_html=graph_html)
    



@app.route('/perfil')
def perfil():
    
        return render_template('perfil.html')

@app.route('/log_in')
def log_in():
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        USERNAME=usuario
        PASSWORD=contraseña
      
        
        if username == USERNAME and password == PASSWORD:
            session['username'] = username  
            flash('Inicio de sesión')
            return redirect(url_for(''))
        else:
            flash('error')
            return redirect(url_for('log_in'))
   

     return render_template('log_in.html') 


if __name__ == '__main__':
    app.run(debug=True, port=3500)
