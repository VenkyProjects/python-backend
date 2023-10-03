LoginTableQuery='''
        CREATE TABLE login_table (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            user_name VARCHAR(50),
            password VARCHAR(50)
        );
    '''

from peewee import *
from playhouse.postgres_ext import UUIDField, fn
from fastapi import HTTPException
import re

db = PostgresqlDatabase('sample', host='localhost', port=5432)

class loginTable(Model):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    user_name = CharField()
    password = CharField  ()

    class Meta:
        database = db
        table_name = 'login_table'
    
    def  validate_username_password(self):
        if self.user_name and self.password:
            raise HTTPException(status_code=500,detail="useranme and password already exists")
        else:
            return  True
    
    


