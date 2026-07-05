from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from .database import Base ,engine 
from .routes import router 

#creation de toutes les tables
Base.metadata.create_all(bind=engine)

#creation de l'application 
app = FastAPI(title = "contacts API" , version = "1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#enrehistrement des outjes 
app.include_router(router)
