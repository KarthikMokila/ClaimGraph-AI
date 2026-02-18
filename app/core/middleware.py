import uuid
from fastapi import Request
from app.core.logging import logger
from starlette.middleware.base import BaseHTTPMiddleware

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        bound_logger = logger.bind(request_id = request_id)
        request.state.logger = bound_logger

        response = await call_next(request)

        response.headers['X-Request-ID'] = request_id

        return response