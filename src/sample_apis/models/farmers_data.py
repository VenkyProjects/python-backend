FarmersDataQuery='''
        CREATE TABLE FarmersData_table (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            name VARCHAR(50),
            crop VARCHAR(50),
            acres VARCHAR(50),
            urea VARCHAR(50),
            pesticides VARCHAR(50),
            amount VARCHAR(50),
            quintals VARCHAR(50)
        );
    '''

from peewee import *
from playhouse.postgres_ext import UUIDField, fn
from fastapi import HTTPException

db = PostgresqlDatabase('sample', host='localhost', port=5432)

class farmerDataTable(Model):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    name = CharField()
    crop = CharField  ()
    acres = CharField  ()
    urea = CharField  ()
    pesticides = CharField  ()
    amount = CharField  ()
    quintals= CharField  ()

    class Meta:
        database = db
        table_name = 'farmersdata_table'
    
    def detail(self):
        total_amount=(int(self.quintals)*int(self.amount))-(int(self.urea)*(290))
        return{
            'total_amount':total_amount
        }