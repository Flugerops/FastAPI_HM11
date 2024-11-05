from typing import Annotated

from fastapi import Depends, APIRouter

from ..utils import oauth2_scheme


items_router = APIRouter(prefix="/items", tags=["items"])


@items_router.get("/info", summary="Get access token", deprecated=True)
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@items_router.get(
    "/all_items",
    summary="Items mock",
    description="Returns a mock data of items",
    response_description="List of items(dictionaries)",
)
async def items_list():
    return [{"title": "mock1", "value": 15}, {"title": "mock2", "value": 40}]
