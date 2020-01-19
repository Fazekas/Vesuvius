from flask import request, jsonify, Blueprint
from models import card_model
from schemas import card_schema
from vesuvius import db

cardBP = Blueprint('card_blueprint', __name__)


def say_hello():
    return 'hello'


# Create a Product
@cardBP.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['qty']

    new_product = card_model.Product(name, description, price, quantity)

    db.session.add(new_product)
    db.session.commit()

    return card_schema.product_schema.jsonify(new_product)


# Get all products
@cardBP.route('/product', methods=['GET'])
def get_products():
    all_products = card_model.Product.query.all()
    result = card_schema.products_schema.dump(all_products)
    return jsonify(result)


# Get product
@cardBP.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = card_model.Product.query.get(product_id)
    return card_schema.product_schema.jsonify(product)


# Update a Product
@cardBP.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = card_model.Product.query.get(product_id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()
    return card_schema.product_schema.jsonify(product)


# Delete a Product
@cardBP.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = card_model.Product.query.get(product_id)

    db.session.delete(product)
    db.session.commit()
    return card_schema.product_schema.jsonify(product)


@cardBP.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})
