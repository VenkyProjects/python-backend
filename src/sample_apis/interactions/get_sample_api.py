from sample_apis.models.sample_api import SampleTable

def get_sample_api(request):
    details={}
    
    if all_fields_present(request):
        object=SampleTable.select().where(
            SampleTable.name==request.get("name"),
        ).first()
        
        if object:
          details = object.detail()
    else:
       return {}
    
    return details

def all_fields_present(request):
   if request.get('name'):
      return True
   return False
   