from pydantic import BaseModel

class CreateSampleApiParams(BaseModel):
    name:str=None
    age:str=None
    phone:str=None

class CreateFarmerDataApiParams(BaseModel):
    name:str=None
    crop:str=None
    acres:str=None
    urea:str=None
    pesticides:str=None
    amount:str=None
    quintals:str=None
    
class GetFarmerDataApiParams(BaseModel):
    id:str=None
    



class UpdateSampleApiParams(BaseModel):
    id:str
    name:str=None
    age:str=None
    phone:str=None

class DeleteSampleApisParams(BaseModel):
    id:str

class LoginAccountApiParams(BaseModel):
    user_name:str
    password:str

class CretaeAccountApiParams(BaseModel):
    user_name:str
    password:str