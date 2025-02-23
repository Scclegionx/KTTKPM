# book/models.py
from mongoengine import Document, StringField, DecimalField, IntField, DateField, FloatField

class Book(Document):
    meta = {'collection': 'book'}
    title = StringField(max_length=255, required=True)
    author = StringField(max_length=255, required=True)
    price = DecimalField(precision=2, required=True)
    stock = IntField(min_value=0, required=True)
    description = StringField()
    published_date = DateField(required=True)
    genre = StringField(max_length=100)
    rating = FloatField(default=0.0)

    def __str__(self):
        return self.title
