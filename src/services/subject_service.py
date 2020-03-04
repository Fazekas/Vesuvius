from flask import request, jsonify, Blueprint, send_file
from ..entities import subject_entity
from ..schemas import subject_schema
from ..dbms.rdb import db


def add_subject():
    name = request.json['name']

    new_subject = subject_entity.Subject(name)

    db.session.add(new_subject)
    db.session.commit()

    return subject_schema.subject_schema.jsonify(new_subject)


def get_subjects():
    all_subjects = subject_entity.Subject.query.all()
    result = subject_schema.subjects_schema.dump(all_subjects)
    return jsonify(result)

def get_subject(subject_id):
    subject = subject_entity.Subject.query.get(subject_id)
    return subject_schema.subject_schema.jsonify(subject)


def update_subject(subject_id):
    subject = subject_entity.Subject.query.get(subject_id)
    name = request.json['name']

    subject.name = name

    db.session.commit()
    return subject_schema.subject_schema.jsonify(subject)

def delete_subject(subject_id):
    subject = subject_entity.Subject.query.get(subject_id)

    db.session.delete(subject)
    db.session.commit()
    return subject_schema.subject_schema.jsonify(subject)

def get():
    return send_file('./images/exoplanet.jpg')