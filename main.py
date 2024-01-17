from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError

app = FastAPI()


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@app.get("/")
async def read_root():
    return "Hello, world!"


# @app.post("/api/v1/groups")
# async def create_group(number: int, symbol: str):
#     pass
#
#
# @app.get("/api/v1/groups")
# async def get_all_groups():
#     pass


@app.get("/api/v1/groups/{group_id}")
async def get_group_by_id(group_id: int):
    return {"group_id": group_id}


# @app.put("/api/v1/groups/{group_id}")
# async def update_group_by_id(group_id: int, number: int = None, symbol: str = None):
#     pass
#
#
# @app.delete("/api/v1/groups/{group_id}")
# async def delete_group_by_id(group_id: int):
#     pass
