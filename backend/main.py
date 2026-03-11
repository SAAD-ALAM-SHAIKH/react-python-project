from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # pyright: ignore[reportMissingImports]

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Login(BaseModel):
    username: str
    password: str


@app.get("/")
def home():
    return {"message": "FastAPI backend connected!"}


@app.post("/login")
def login(data: Login):

    if data.username == "admin" and data.password == "1234":
        return {"status": "success", "message": "Login successful"}

    return {"status": "error", "message": "Invalid credentials"}