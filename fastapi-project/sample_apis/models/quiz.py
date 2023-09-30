CreateQuizQuery = '''
        CREATE TABLE quiz_table (
            question_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            question_text VARCHAR(100),
            options text[],
            correct_answer VARCHAR(50),
            category VARCHAR(50),
            difficulty_level VARCHAR(50),
            explanation_text VARCHAR(50),
            user_response JSONB[],
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            answered_at TIMESTAMP WITH TIME ZONE,
            quiz_metadata JSONB,
            tags VARCHAR(50),
            is_active BOOLEAN DEFAULT true,
            question_type VARCHAR(50),
            image_url VARCHAR(50),
            custom_field1 VARCHAR(50),
            custom_field2 VARCHAR(50),
            custom_field3 VARCHAR(50)
        );
    '''

from peewee import *
from playhouse.postgres_ext import UUIDField, fn
from fastapi import HTTPException

db = PostgresqlDatabase('sample', host='localhost', port=5432)

class Quiztable(Model):
    question_id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    question_text=CharField(null=True)
    correct_answer=CharField(null=True)
    category=CharField(null=True)
    difficulty_level=CharField(null=True)
    explanation_text=CharField(null=True)
    tags=CharField(null=True)
    options=CharField(null=True)
    question_text=CharField(null=True)
    is_active=BooleanField(null=True,default=True)

    class Meta:
        database = db
        table_name = 'quiz_table'
        

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
    
    
