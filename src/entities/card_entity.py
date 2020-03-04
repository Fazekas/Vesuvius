from ..dbms.rdb import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    question = db.Column(db.String(200))
    answer = db.Column(db.String(200))
    picture = db.Column(db.String(200))

    def __init__(self, answer, question, picture, subject_id):
        self.question = question
        self.answer = answer
        self.picture = picture
        self.subject_id = subject_id
