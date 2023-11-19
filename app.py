from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os



# Crear una instancia de la aplicación Flask sqlite:///database/data_form1.sqlite3--sqlite:database/data_form1.sqlite3
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.static_folder = 'static'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data_form1.sqlite3'
#db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database/data_form1.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita la advertencia de seguimiento

db = SQLAlchemy(app)
#clases - model

class InformacionForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    telefono = db.Column(db.String(20))
    link = db.Column(db.String(64))
    nombre_empresa = db.Column(db.String(40))
    email = db.Column(db.String(40))
    observaciones = db.Column(db.String(2000))

# Rutas y vistas
@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/welcome.html')
def welcome():
    return render_template('welcome.html')

@app.route('/nosotros.html')
def nosotros():
    return render_template('/nosotros.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

#propuestas

@app.route('/propuesta1')
def propuesta1():
    return render_template('propuesta1.html')

@app.route('/propuesta2')
def propuesta2():
    return render_template('propuesta2.html')

@app.route('/propuesta3')
def propuesta3():
    return render_template('propuesta3.html')

#========================


#=========================
#base de datos 

#@app.route('/create_db', methods=['POST'])
#def create():
#    data_save1 = data_save(nombre=request.fomr['nombre'])
#    db.session.add
#    db.session.commit()

@app.route("/create_db", methods=["POST"])
def create_db():
    try:
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        link = request.form["link"]
        nombre_empresa = request.form["nombre_empresa"]  # Ajustado al nombre correcto del formulario
        email = request.form["email"]
        observaciones = request.form["observaciones"]

        # Guarda los datos en la base de datos
        nuevo_registro = InformacionForm(nombre=nombre, telefono=telefono, link=link, nombre_empresa=nombre_empresa, email=email, observaciones=observaciones)
        db.session.add(nuevo_registro)
        db.session.commit()

        return redirect("/")

    except Exception as e:
        # Maneja cualquier error, por ejemplo, si no se pueden guardar los datos
        return f"Error: {str(e)}"



if __name__ == '__main__':
    app.run()

