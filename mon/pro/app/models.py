from mongoengine import Document, StringField, IntField






class Try_2(Document):
    title = StringField(max_length=100)
    body = StringField(max_length=100)