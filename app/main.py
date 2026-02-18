from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import setup_logging
from app.core.middleware import RequestIDMiddleware

setup_logging()

app = FastAPI(
    title = "ClaimGraph AI",
    description= "Processing claims using LangGraph"
)
app.add_middleware(RequestIDMiddleware)
app.include_router(router)