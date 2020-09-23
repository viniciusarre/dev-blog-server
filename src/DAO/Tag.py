from mongoengine import BooleanField, Document, StringField, ObjectIdField


class Tag(Document):
    _id = ObjectIdField()
    name = StringField(required=True)
    color = StringField(required=True)
