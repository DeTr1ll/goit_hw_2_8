from mongoengine import Document, StringField, ReferenceField, ListField, BooleanField, connect

connect(db="HumiderCluster", host="mongodb+srv://Humider:4U7m5q80uf0UaSZo@humidercluster.5in6y.mongodb.net/?retryWrites=true&w=majority&appName=HumiderCluster")

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
    phone = StringField()
    address = StringField()