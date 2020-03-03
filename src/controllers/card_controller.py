from flask import request, jsonify, Blueprint, send_file
from ..entities import card_entity
from ..schemas import card_schema
from ..dbms.rdb import db

card_blueprint = Blueprint('card', __name__, url_prefix='/card')


# Create a Card mutation
@card_blueprint.route('/card', methods=['POST'])
def add_card():
    question = request.json['question']
    answer = request.json['answer']
    picture = request.json['picture']
    subject_id = request.json['subject_id']

    new_product = card_entity.Card(question, answer, picture, subject_id)

    db.session.add(new_product)
    db.session.commit()

    return card_schema.card_schema.jsonify(new_product)


# # Get all cards query
@card_blueprint.route('/cards', methods=['GET'])
def get_cards():
    all_cards = card_entity.Card.query.all()
    result = card_schema.cards_schema.dump(all_cards)
    return jsonify(result)


# # Get card query
@card_blueprint.route('/card/<card_id>', methods=['GET'])
def get_card(card_id):
    card = card_entity.Card.query.get(card_id)
    return card_schema.card_schema.jsonify(card)


# # Update a card mutation
@card_blueprint.route('/card/<card_id>', methods=['PUT'])
def update_card(card_id):
    card = card_entity.Card.query.get(card_id)
    question = request.json['question']
    answer = request.json['answer']
    picture = request.json['picture']

    card.question = question
    card.answer = answer
    card.picture = picture

    db.session.commit()
    return card_schema.card_schema.jsonify(card)


# # Delete a card mutation
@card_blueprint.route('/card/<card_id>', methods=['DELETE'])
def delete_card(card_id):
    product = card_entity.Card.query.get(card_id)

    db.session.delete(product)
    db.session.commit()
    return card_schema.product_schema.jsonify(product)


# Test route that returns a picture
@card_blueprint.route('/', methods=['GET'])
def get():
    return send_file('./images/swissWinterNight.jpg')
