from flask import request, jsonify, Blueprint, send_file
# from ..entities import subject_entity
# from ..schemas import subject_schema
# from ..dbms.rdb import db

from ..services import subject_service

subject_blueprint = Blueprint('subject', __name__, url_prefix='/subject')


# Create a Subject mutation
@subject_blueprint.route('/subject', methods=['POST'])
def add_subject():
    return subject_service.add_subject()


# Get all Subjects query
@subject_blueprint.route('/subjects', methods=['GET'])
def get_subjects():
    return subject_service.get_subjects()


# Get Subject query
@subject_blueprint.route('/subject/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    return subject_service.get_subject(subject_id)


# Update a Subject mutation
@subject_blueprint.route('/subject/<subject_id>', methods=['PUT'])
def update_subject(subject_id):
    return subject_service.update_subject(subject_id)

# Delete a card mutation
@subject_blueprint.route('/subject/<subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    return subject_service.delete_subject(subject_id)


# Test route that returns a picture
@subject_blueprint.route('/', methods=['GET'])
def get():
    return subject_service.get()
