from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

username = "alex"
password = "FXAvNwD1BHLf6AdH"
host = "oleksandr.jpirka4.mongodb.net"

# uri = 'mongodb+srv://<username>:<password>@oleksandr.jpirka4.mongodb.net/'
URI = f"mongodb+srv://{username}:{password}@{host}/"

connect(db="Web-HW-8-1", host=URI)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)
    tags = ListField(StringField(max_length=35))
    meta = {"collection": "quotes"}

