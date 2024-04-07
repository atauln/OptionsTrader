from datetime import datetime
from fastapi import FastAPI, HTTPException
from db import application_layer, service_layer
from routers import account, asset

app = FastAPI()

# create routers for each subdirectory
app.include_router(account.router, tags=["accounts"])
app.include_router(asset.router, tags=["assets"])

