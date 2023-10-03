from sample_apis.models.farmers_data import farmerDataTable

def get_farmer_data_api(request):
    data=farmerDataTable.select().where(
        farmerDataTable.id==request.get('id')
    ).first()

    details={}
    if data:
        details=data.detail()
    
    return details
