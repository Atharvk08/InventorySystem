from mongoengine import Document, StringField, DecimalField, IntField,ReferenceField
from suppliers.models import Supplier

class Product(Document):
    name=StringField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    price = StringField(required=True)
    stock_quantity = IntField(required=True)
    supplier = ReferenceField(Supplier, required=True)

    def __str__(self):
        return self.name
