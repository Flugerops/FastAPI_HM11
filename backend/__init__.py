from fastapi import FastAPI, APIRouter


app = FastAPI(debug=True)

from .routes import auth_router, items_router


app.include_router(auth_router)
app.include_router(items_router)
