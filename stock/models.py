from mongoengine import Document, IntField, StringField, DateField,ReferenceField
from products.models import Product

class StockMovement:
    product = ReferenceField(Product, required = True)
    quantity = IntField(required = True)
    movement_type= StringField(required = True)
    movement_date=DateField(required = True)
    notes = StringField()
    