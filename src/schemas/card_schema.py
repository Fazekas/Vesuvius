from .marshmallow import ma


class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'subject_id', 'question', 'answer', 'picture')


# Init schema
card_schema = CardSchema()
cards_schema = CardSchema(many=True)
