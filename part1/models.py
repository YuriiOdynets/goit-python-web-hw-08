import mongoengine as me

class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField(required=True)
    born_location = me.StringField(required=True)
    description = me.StringField(required=True)

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)
    quote = me.StringField(required=True)