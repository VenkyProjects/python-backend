from sample_apis.models.login_api import loginTable
from fastapi import HTTPException


def login_account_api(request):
    data=loginTable.select().where(
        loginTable.user_name==request.get("user_name"),
        loginTable.password==request.get("password"),
    ).first()

    if data.password and data.user_name:
        return {'id':str(data.id),'detail':'login successully'}
    else:
        raise HTTPException(status_code=400, detail="username or password is incorrect")
    
    # if not data:
        # raise HTTPException(status_code=400, detail="username or password is incorrect")
    

    