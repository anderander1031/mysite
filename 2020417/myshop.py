from flask import Flask, render_template

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15, "desc": "This is a pen.", "image":"https://dictionary.cambridge.org/zht/images/thumb/pen_noun_002_27028.jpg?version=5.0.75"},
  "sku02": { "id": "sku02", "name": "Cup", "price": 80, "desc": "This is a cup.", "image":"https://dictionary.cambridge.org/zht/images/thumb/cup_noun_002_09489.jpg?version=5.0.75"},
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25, "desc": "great notebook", "image":"https://dictionary.cambridge.org/zht/images/thumb/spiral_noun_002_35207.jpg?version=5.0.75"},
  "sku04": { "id": "sku04", "name": "Stapler", "price": 20, "desc": "useful stapler", "image":"https://images-na.ssl-images-amazon.com/images/I/61GZIr9bcxL._AC_SX466_.jpg"},
}

cart = {
  "sku01": 2,
  "sku02": 5
}

app = Flask(__name__)

@app.route("/")
def myshop():
    return render_template("myshop.html", products=products, cart=cart)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)