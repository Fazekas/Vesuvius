from flask import request, jsonify, Blueprint, send_file
from ..entities import card_entity
from ..schemas import card_schema
from ..dbms.rdb import db



def add_card():
    question = request.json['question']
    answer = request.json['answer']
    picture = request.json['picture']
    subject_id = request.json['subject_id']

    new_card = card_entity.Card(question, answer, picture, subject_id)

    db.session.add(new_card)
    db.session.commit()

    return card_schema.card_schema.jsonify(new_card)


def get_cards():
    all_cards = card_entity.Card.query.all()
    result = card_schema.cards_schema.dump(all_cards)
    return jsonify(result)

def get_card(card_id):
    card = card_entity.Card.query.get(card_id)
    return card_schema.card_schema.jsonify(card)


def update_card(card_id):
    card = card_entity.Card.query.get(card_id)
    question = request.json['question']
    answer = request.json['answer']
    picture = request.json['picture']
    subject_id = request.json['subject_id']

    card.question = question
    card.answer = answer
    card.picture = picture
    card.subject_id = subject_id

    db.session.commit()
    return card_schema.card_schema.jsonify(card)


def delete_card(card_id):
    card = card_entity.Card.query.get(card_id)

    db.session.delete(card)
    db.session.commit()
    return card_schema.card_schema.jsonify(card)


def get():
    return send_file('./images/swissWinterNight.jpg')