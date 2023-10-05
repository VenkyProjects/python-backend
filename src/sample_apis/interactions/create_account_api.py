from sample_apis.models.login_api import loginTable
from fastapi import HTTPException
import re

def create_account_api(request):
    row={
        'user_name':request.get("user_name"),
        'password':request.get("password")
    }
    data=loginTable.select().where(
        loginTable.user_name==request.get('user_name'),
        # loginTable.password==request.get('password')
    ).first()
    
    if not data:
        data=loginTable(**row)
        
    else:
        data.validate_username_password()

    try:
        data.save()

    except HTTPException as e:
        raise HTTPException(status_code=400, detail="Data did not save")
    
    return {'id':str(data.id)}


    
