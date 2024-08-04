import mongoengine as me

class Contact(me.Document):
    fullname = me.StringField(required = True)
    email = me.StringField(required = True)
    message_sent = me.BooleanField(default=False)
    phone = me.StringField()
    address = me.StringField()
    company = me.StringField()