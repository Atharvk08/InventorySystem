from mongoengine import Document, StringField, EmailField

class Supplier(Document):
    name = StringField(required = True)
    email= EmailField(required= True, unique =True)
    phone = StringField(required = True)
    address = StringField(requried = True)

    def __str__(self):
        return self.name