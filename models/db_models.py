from datetime import datetime

import mongoengine as me


class Users(me.Document):
    phone_no = me.IntField(required=True, unique=True)
    first_name = me.StringField()
    last_name = me.StringField()
    city = me.StringField()
    registered_at = me.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return "User<phone_no={}>".format(self.phone_no)


class Activity(me.Document):
    phone_no = me.IntField(required=True)
    item = me.StringField(required=True)
    calorie = me.DecimalField(default=0)
    protein = me.DecimalField(default=0)
    quantity = me.DecimalField()
    sugar = me.DecimalField(default=0)
    category = me.StringField()
    recorded_at = me.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return "Activity(item={},phone_no={})".format(self.item, self.phone_no)
