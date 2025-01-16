from mongoengine import ReferenceField, IntField, DecimalField, DateField, StringField
from products.models import Product

class SalesOrder:
    product = ReferenceField(Product, required = True)
    quantity = IntField(required = True)
    total_price = DecimalField(required = True)
    sale_date = DateField(required = True)
    status = StringField(required = True)
