CreateMusicQuery = '''
        CREATE TABLE music_table (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            url VARCHAR(50),
            is_active BOOL DEFAULT true
        );
    '''

from peewee import *
from playhouse.postgres_ext import UUIDField, fn
from fastapi import HTTPException

db = PostgresqlDatabase('sample', host='localhost', port=5432)

class MusicTable(Model):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    url=CharField(null=True)
    is_active=BooleanField(null=True,default=True)

    class Meta:
        database = db
        table_name = 'sample_table'
        

    def detail(self):
        return {
            "name":self.name,
            "age":self.age,
            "id":self.id,
            "phone":self.phone
        }
    def validate_phone(self):
        if self.phone and len(self.phone)==10:
            return True
        else:
            raise HTTPException(status_code=500, detail ="phone number should be 10 ")
        
    def validate(self):
        self.validate_phone()

    def validate_age(self):
        if int(self.age)>10:
            return True
        else:
            raise HTTPException(status_code=500,detail="age should be greater than 10")
    
    

