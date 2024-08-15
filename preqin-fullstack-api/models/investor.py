from peewee import *

db = SqliteDatabase('investor.db')

class Investor(Model):
  investor_name = CharField()
  investory_type = CharField()
  investor_country = CharField()
  investor_date_added = DateField()
  investor_last_updated = DateField()
  commitment_asset_class = CharField()
  commitment_amount = FloatField()
  commitment_currency = CharField()
  
  class Meta:
    database = db