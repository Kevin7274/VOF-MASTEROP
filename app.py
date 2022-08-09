from flask import Flask, render_template

app = Flask(__name__)

####### Rutas public #######

@app.route('/')
def index():  
    return render_template('public/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('public/nosotros.html')

@app.route('/productos')
def productos():
    productos = [
        {
            'imagen':'img/BAD.jpg',
            'name':'Chaqueta BAD',
            'material':'Material: Gabardina',
            'precio':'2500',
            'href':'Comprar'
        },
        {
            'imagen':'img/thriller.jpg',
            'name':'Chaqueta THRILLER',
            'material':'Material: Cuero sintetico',
            'precio':'1500',
            'href':'Comprar'
        },   
        {
            'imagen':'img/cte.jpg',
            'name':'Camisas CTE',
            'material':'Material: Poliester',
            'precio':'450',
            'href':'Comprar'
        },
        {
            'imagen':'img/beat.jpg',
            'name':'Chaqueta BEAT IT',
            'material':'Material: Piel',
            'precio':'3000',
            'href':'Comprar'
        },
        {
            'imagen':'img/beatit.jpg',
            'name':'Chaqueta BEAT IT (imitacion)',
            'material':'Material: Charol ',
            'precio':'1500',
            'href':'Comprar'
        },
        {
            'imagen':'img/thrillerh.jpg',
            'name':'Chaqueta THRILLER History Tour',
            'material':'Material: Charol y Cuero Sintetico ',
            'precio':'1800',
            'href':'Comprar'
        },
        {
            'imagen':'img/BTH.jpg',
            'name':'Chaqueta BEAT IT History Tour',
            'material':'Material: Cuero Sintetico ',
            'precio':'2000',
            'href':'Comprar'
        },
        {
            'imagen':'img/smooth.jpg',
            'name':'Saco SMOOTH CRIMINAL History Tour',
            'material':'Material: Casimir Español ',
            'precio':'1800',
            'href':'Comprar'
        },
        {
            'imagen':'img/history.jpg',
            'name':'Traje HISTORY TOUR',
            'material':'Material: Licra Metalica',
            'precio':'1200',
            'href':'Comprar'
        },
        {
            'imagen':'img/another.jpg',
            'name':'Traje BAD TOUR',
            'material':'Material: Licra Metalica',
            'precio':'700',
            'href':'Comprar'
        },
        {
            'imagen':'img/saco.jpg',
            'name':'Saco BAD TOUR',
            'material':'Material: Gabardina',
            'precio':'1200',
            'href':'Comprar'
        },
        {
            'imagen':'img/leotardo.jpg',
            'name':'Leotardo DANGEROUS TOUR',
            'material':'Material: Licra Metalica',
            'precio':'700',
            'href':'Comprar'
        },
        {
            'imagen':'img/jam1992.jpg',
            'name':'Vestuario JAM 1992',
            'material':'Material: Tergal Tornasol',
            'precio':'1500',
            'href':'Comprar'
        },
        {
            'imagen':'img/jam1993.jpg',
            'name':'Vestuario JAM 1993',
            'material':'Material: Gabardina Y latón',
            'precio':'3500',
            'href':'Comprar'
        },
        {
            'imagen':'img/remember.jpg',
            'name':'Vestuario REMEMBER THE TIME',
            'material':'Material: Licra Y latón',
            'precio':'5000',
            'href':'Comprar'
        },
        {
            'imagen':'img/capitan.jpg',
            'name':'Vestuario CAPTAIN EO',
            'material':'Material: Leds y Royal Japones',
            'precio':'15000',
            'href':'Comprar'
        },
        {
            'imagen':'img/teaser.jpg',
            'name':'Vestuario HISTORY TEASER',
            'material':'Material: Gabardina Japonesa',
            'precio':'5000',
            'href':'Comprar'
        },
        {
            'imagen':'img/eo.jpg',
            'name':'Chaqueta FREDDY MERCURY',
            'material':'Material: Cuero Sintetico',
            'precio':'650',
            'href':'Comprar'
        },
        {
            'imagen':'img/gaga.jpg',
            'name':'Vestuario LADY GAGA',
            'material':'Material: Tergal',
            'precio':'600',
            'href':'Comprar'
        },
        {
            'imagen':'img/playeras.jpg',
            'name':'Playera TECLAS',
            'material':'Material: Lana',
            'precio':'200',
            'href':'Comprar'
        },
        {
            'imagen':'img/olodum.jpg',
            'name':'Playera OLODUM',
            'material':'Material: Lana',
            'precio':'200',
            'href':'Comprar'
        },
        {
            'imagen':'img/interpol.jpg',
            'name':'Playera INTERPOL',
            'material':'Material: Lana',
            'precio':'200',
            'href':'Comprar'
        },
        {
            'imagen':'img/guns.jpg',
            'name':'Playera GUNS N\' ROSES',
            'material':'Material: Lana',
            'precio':'200',
            'href':'Comprar'
        },
        {
            'imagen':'img/guns2.jpg',
            'name':'Playera GUNS N ROSES',
            'material':'Material: Lana',
            'precio':'200',
            'href':'Comprar'
        },
        {
            'imagen':'img/moon.jpg',
            'name':'CD DARKSIDE OF THE MOON',
            'material':'Genero: Rock',
            'precio':'300',
            'href':'Comprar'
        },
        {
            'imagen':'img/Sin título.jpg',
            'name':'CD THIRLLER',
            'material':'Genero: Pop and Rb',
            'precio':'150',
            'href':'Comprar'
        },
        {
            'imagen':'img/zeppelin.jpg',
            'name':'CD LED ZEPPELIN IV',
            'material':'Genero: Rock and Blues',
            'precio':'150',
            'href':'Comprar'
        }
    ]
    # Cobsulta a BD para recuperar productos
    return render_template('public/productos.html', productos=productos)

@app.route('/contacto')
def contacto():
    return render_template('public/contacto.html')

@app.route('/carrito')
def carrito():
    return render_template('public/carrito.html')

@app.route('/paypal')
def paypal():
    return render_template('public/paypal.html')

####### Rutas #######

@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/formulario')
def formulario():
    return render_template('auth/formulario.html')


if  __name__ == '__main__':
    app.run(debug=True)