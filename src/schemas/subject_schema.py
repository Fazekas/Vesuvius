from .marshmallow import ma


class SubjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


# Init schema
subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)
