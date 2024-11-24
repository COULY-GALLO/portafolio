from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.secret_key = 'patri'

    # Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://upn5pvkmedamkc78:0sIhj9xMhaMKMr0rqAA9@b1cc4uulzyfxlt3zzosj-mysql.services.clever-cloud.com:3306/b1cc4uulzyfxlt3zzosj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(500), nullable=False)

# Crear la base de datos y la tabla
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    experiencias = Experiencia.query.all()
    user_logged_in = 'user' in session  # Verificar si hay sesión iniciada
    return render_template("home.html", experiencias=experiencias, user_logged_in=user_logged_in)

@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "a" and password == "a": 
            session['user'] = username
            return redirect("/")
        else:
            return "Credenciales inválidas", 401
    return render_template("log_in.html")

@app.route('/logout')
def logout():
    session.clear()  
    return render_template('log_out.html')  


@app.route("/añadir_experiencia", methods=["POST"])
def añadir_experiencia():
    if 'user' not in session:
        return "No autorizado", 403
    descripcion = request.form.get("descripcion")
    if descripcion:
        nueva_experiencia = Experiencia(descripcion=descripcion)
        db.session.add(nueva_experiencia)
        db.session.commit()
        return redirect("/")
    return "Error al añadir experiencia", 400

@app.route("/editar_experiencia", methods=["POST"])
def editar_experiencia():
    if 'user' not in session:
        return "No autorizado", 403
    experiencia_id = request.form.get("id")
    descripcion = request.form.get("experiencia")
    experiencia = Experiencia.query.get(experiencia_id)
    if experiencia and descripcion:
        experiencia.descripcion = descripcion
        db.session.commit()
        return redirect("/")
    return "Error al editar experiencia", 400

@app.route("/eliminar_experiencia", methods=["POST"])
def eliminar_experiencia():
    if 'user' not in session:
        return "No autorizado", 403
    experiencia_id = request.form.get("id")
    experiencia = Experiencia.query.get(experiencia_id)
    if experiencia:
        db.session.delete(experiencia)
        db.session.commit()
        return jsonify({"success": True})
    return jsonify({"success": False}), 400






if __name__ == '__main__':
    app.run(debug=True, port=3500)