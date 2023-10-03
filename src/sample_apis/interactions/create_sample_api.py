from sample_apis.models.sample_api import SampleTable
from fastapi import HTTPException
from sample_apis.database.db_session import db

def create_sample_api(request):
    row = {
        'name': request.get("name"),
        'age': request.get("age"),
        "phone":request.get("phone")
    }
    
    data = SampleTable.select().where(
        SampleTable.name == request['name'],
    ).first()

    if not data:
        data=SampleTable(**row)

    for key , value in request.items():
        setattr(data,key,value)
    data.validate()
    try:
        data.save()

    except HTTPException as e:
        raise HTTPException(status_code=400, detail="Data did not save")

    return {'id': str(data.id)}
