from sample_apis.models.sample_api import SampleTable
from fastapi import HTTPException

def delete_sample_api(request):
    data=SampleTable.select().where(
        SampleTable.id==request.get('id')
    ).first()

    if not data:
        raise HTTPException(
            status_code=400, detail="ids are invalid"
        )
    data.is_active=False
    try:
        data.save()
    except:
        raise HTTPException(status_code=500, detail="error in saving")

    return {"id": data.id}
