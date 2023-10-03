from sample_apis.database.db_session import db 
from sample_apis.models.sample_api import SampleTable
from fastapi import HTTPException

def update_sample_api(request):
    # with db.atomic():
    return execute_transaction_code(request)

def execute_transaction_code(request):
    update_api=SampleTable.select().where(SampleTable.id==request.get('id')).first()
    
    if not update_api:
        raise HTTPException(status_code=400, detail=" data not found")
    update_api.name=request.get("name")
    update_api.age=request.get("age")
    update_api.phone=request.get("phone")
    update_api.validate_age()
    update_api.validate_phone()


    try:
        update_api.save()
    except Exception:
        raise HTTPException(status_code=500, detail="data not updated")
    
    return {'id':str(update_api.id)}