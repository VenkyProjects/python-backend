from sample_apis.models.farmers_data import farmerDataTable
from fastapi import HTTPException

def create_farmer_account_api(request):
    print(request)
    row={
        'name':request.get('name'),
        'crop':request.get('crop'),
        'acres':request.get('acres'),
        'urea':request.get('urea'),
        'pesticides':request.get('pesticides'),
        'amount':request.get('amount'),
        'quintals':request.get('quintals')
    }

    data=farmerDataTable.select().where(
        farmerDataTable.name==request.get('name')
    )

    if not data:
        data=farmerDataTable(**row)
    
    data.save()

    return {'id': str(data.id)}