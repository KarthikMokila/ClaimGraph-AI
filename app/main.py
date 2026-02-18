from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "ClaimGraph AI",
    description= "Processing claims using LangGraph"
)

app.include_router(router)