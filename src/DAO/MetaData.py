from mongoengine import BooleanField, Document, StringField, ObjectIdField


class MetaData(Document):
    _id: ObjectIdField(),
    tags: [ObjectIdField],
    strapline: StringField(required=True),
