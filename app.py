from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


# Crear una instancia de la aplicación Flask
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.static_folder = 'static'


# Rutas y vistasx
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

#@app.route('/contacto.html')
#def contacto():
#    return render_template('contacto.html')

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

if __name__ == '__main__':
    app.run()

