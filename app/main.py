import secrets
import string

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET"],
)


@app.get("/api/v1/password/{length}", response_class=ORJSONResponse)
async def password(length: int):
    if length < 10:
        raise HTTPException(status_code=415, detail="Minimum length is 10")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return ORJSONResponse({"password": password})
