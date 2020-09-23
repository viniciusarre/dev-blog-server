from mongoengine import BooleanField, Document, StringField, ObjectIdField


class Comment (Document):
    _id = ObjectIdField()
    user = StringField(required=True)
    comment = StringField(required=True)
    is_thread = BooleanField(default=False),
    next_comment = ObjectIdField()
