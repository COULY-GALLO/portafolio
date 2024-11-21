import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = 'patri'


usuario = os.getenv("USUARIO")
contraseña = os.getenv("CONTRASEÑA")

def load_experiences(filepath='experiencias.json'):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_experiences(experiencias, filepath='experiencias.json'):
    with open(filepath, 'w') as file:
        json.dump(experiencias, file)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/perfil')
def perfil():
    experiencias = load_experiences()
    return render_template('perfil.html', experiencias=experiencias)


@app.route('/editar_experiencia', methods=['POST'])
def editar_experiencia():
    if 'username' not in session:
        flash('Debe iniciar sesión para editar.')
        return redirect(url_for('log_in'))

    nueva_experiencia = request.form.get('experiencia')
    index = int(request.form.get('index'))

   
    experiencias = load_experiences()
    if 0 <= index < len(experiencias):
        experiencias[index] = nueva_experiencia
        save_experiences(experiencias)
        flash('Experiencia actualizada correctamente.')
    else:
        flash('Índice inválido.')

    return redirect(url_for('perfil'))


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']

        if username == usuario and password == contraseña:
            session['username'] = username  
            flash('Inicio de sesión exitoso')
            return redirect(url_for('home')) 
        else:
            flash('Error en usuario o contraseña')
            return redirect(url_for('log_in')) 

    return render_template('log_in.html')


@app.route('/log_out')
def log_out():
    session.pop('username', None) 
    flash('Sesión cerrada.')
    return redirect(url_for('home'))  


if __name__ == '__main__':
    app.run(debug=True, port=3500)
