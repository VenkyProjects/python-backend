from fastapi import FastAPI
import psycopg2
from sample_apis.sample_api_router import sample_api_router
from sample_apis.models.music_list import CreateMusicQuery
from sample_apis.models.sample_api import CreateTableQuery
from sample_apis.models.login_api import LoginTableQuery
from sample_apis.models.quiz import CreateQuizQuery

from dotenv import dotenv_values

#adding cors headers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

#adding cors urls


#add middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods = ["*"],
    allow_headers=["*"]
)


database="sample"

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    # user="your_username",
    # password="your_password",
    database="sample"
)
cursor = conn.cursor()
# cursor.execute(CreateQuizQuery)
conn.commit()
cursor.close()
conn.close()

app.include_router(prefix = "/sample_apis",router = sample_api_router)