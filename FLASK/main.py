from flask import Flask, render_template

app = Flask(__name__)

menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'О нашей продукции', 'url': 'about'},
        {'name': 'Каталог', 'url': 'catalog'},
        {'name': 'Обратная связь', 'url': 'contacts'}
]

catalog_menu = [{'c_name': 'Масло для легковых автомобилей', 'c_url': 'maslodlyalegkovihavto'},
        {'c_name': 'Масло для 4-х тактных двигателей', 'c_url': 'maslodlya2taktnih'},
        {'c_name': 'Масло для 2-х тактных двигателей', 'c_url': 'maslodlya4taktnih'},
        {'c_name': 'Масло для грузовых автомобилей', 'c_url': 'maslodlyagruzovihavto'}
]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нашей продукции', menu=menu)


@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Каталог', menu=menu, catalog_menu=catalog_menu)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
