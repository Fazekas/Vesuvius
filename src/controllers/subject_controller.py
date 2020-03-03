from flask import request, jsonify, Blueprint, send_file
from ..entities import subject_entity
from ..schemas import subject_schema
from ..dbms.rdb import db

subject_blueprint = Blueprint('subject', __name__, url_prefix='/subject')


# Create a Subject mutation
@subject_blueprint.route('/subject', methods=['POST'])
def add_subject():
    name = request.json['name']

    new_subject = card_entity.Card(name)

    db.session.add(new_subject)
    db.session.commit()

    return card_schema.card_schema.jsonify(new_subject)


# # Get all Subjects query
@subject_blueprint.route('/subjects', methods=['GET'])
def get_subjects():
    all_subjects = subject_entity.Subject.query.all()
    result = subject_schema.subjects_schema.dump(all_subjects)
    return jsonify(result)


# # Get Subject query
@subject_blueprint.route('/subject/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    subject = subject_entity.Subject.query.get(subject_id)
    return subject_schema.subject_schema.jsonify(subject)


# # Update a Subject mutation
@subject_blueprint.route('/subject/<card_id>', methods=['PUT'])
def update_subject(subject_id):
    subject = subject_entity.Subject.query.get(subject_id)
    name = request.json['name']

    subject.name = name

    db.session.commit()
    return subject_schema.subject_schema.jsonify(subject)


# # Delete a card mutation
@subject_blueprint.route('/subject/<subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    subject = card_entity.Card.query.get(subject_id)

    db.session.delete(subject)
    db.session.commit()
    return subject_schema.subject_schema.jsonify(subject)


# Test route that returns a picture
@subject_blueprint.route('/', methods=['GET'])
def get():
    return send_file('./images/exoplanet.jpg')
