from fastapi import APIRouter, Query, Depends, HTTPException,Body
from fastapi.responses import JSONResponse
# from rms_utils.auth import authorize_token
from fastapi.encoders import jsonable_encoder
from sample_apis.params import *



# load_dotenv('.env')


from sample_apis.interactions.create_sample_api import create_sample_api
from sample_apis.interactions.get_sample_api import get_sample_api
from sample_apis.interactions.update_sample_api import update_sample_api
from sample_apis.interactions.delete_sample_api import delete_sample_api
from sample_apis.interactions.login_account_api import login_account_api
from sample_apis.interactions.create_account_api import create_account_api
from sample_apis.interactions.create_farmer_account_api import create_farmer_account_api
from sample_apis.interactions.get_farmer_data_api import get_farmer_data_api
from sample_apis.interactions.list_questions_api import list_questions_api

sample_api_router = APIRouter()


@sample_api_router.post("/create_sample_api")
def create_sample_api_data(request: CreateSampleApiParams):
    # if resp["status_code"]!=200:
    #     return JSONResponse(status_code=resp['status_code'],content=resp)
    # try:
        print(request)
        data=create_sample_api(request.dict(exclude_none=False))
        return JSONResponse(status_code=200,content=jsonable_encoder(data))
    # except HTTPException as e :
    #     raise
    # except Exception as e:
    #     # sentry_sdk.capture_exception(e)
    #     return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@sample_api_router.post("/create_farmer_account_api")
def create_farmer_account_api_data(request:CreateFarmerDataApiParams):
    data=create_farmer_account_api(request.dict(exclude_none=False))
    return JSONResponse(status_code=200,content=jsonable_encoder(data))

@sample_api_router.post("/get_farmer_data_api")
def get_farmer_data_api_data(request:GetFarmerDataApiParams):
    data=get_farmer_data_api(request.dict(exclude_none=False))
    return JSONResponse(status_code=200,content=jsonable_encoder(data))
    
@sample_api_router.post("/get_sample_api")
def get_sample_api_data(
    name:str=None,
    # age:str=None,
    # resp: dict = Depends(authorize_token),
):
    # if resp["status_code"] != 200:
    #     return JSONResponse(status_code=resp["status_code"], content=resp)
    request = {
        "name": name,
    }

    try:
        data = get_sample_api(request)
        data = jsonable_encoder(data)
        return JSONResponse(status_code=200, content=data)
    except HTTPException as e:
        raise
    except Exception as e:
        # sentry_sdk.capture_exception(e)
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )
@sample_api_router.get("/list_questions_api")
def list_questions_api_data():
    try:
        data=list_questions_api()
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        # sentry_sdk.capture_exception(e)
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )
@sample_api_router.post("/update_sample_api")
def update_sample_api_data(
    request:UpdateSampleApiParams
):
    # if resp["status_code"] != 200:
    #     return JSONResponse(status_code=resp["status_code"], content=resp)

    try:
        data = update_sample_api(request.dict(exclude_none=True))
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        # sentry_sdk.capture_exception(e)
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )

@sample_api_router.post("/delete_sample_api")
def delete_sample_api_data(request:DeleteSampleApisParams):
    # if resp['status_code']!=200:
    #     return JSONResponse(status_code=resp['status_code'],content=resp)
    try:
        data=delete_sample_api(request.dict(exclude_none=True))
        return JSONResponse(status_code=200,content=jsonable_encoder(data))
    except HTTPException as e:
        raise 
    except Exception as e :
        return JSONResponse(status_code=500 , content={"success":False, "error":str(e)})
    
@sample_api_router.post("/login_account_api")
def login_account_api_data(request:LoginAccountApiParams):
    try:
        data=login_account_api(request.dict(exclude_none=True))
        return JSONResponse(status_code=200,content=jsonable_encoder(data))
    except HTTPException as e:
        raise 
    except Exception as e :
        return JSONResponse(status_code=500 , content={"success":False, "error":str(e)})
    
@sample_api_router.post("/create_account_api")
def create_account_api_data(request:CretaeAccountApiParams):
    # if resp["status_code"]!=200:
    #     return JSONResponse(status_code=resp['status_code'],content=resp)
    try:
        data=create_account_api(request.dict(exclude_none=True))
        return JSONResponse(status_code=200,content=jsonable_encoder(data))
    except HTTPException as e :
        raise
    except Exception as e:
        # sentry_sdk.capture_exception(e)
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })