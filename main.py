from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
load_dotenv()


from api import router
from rate_limiter import limiter

app = FastAPI(title="RAG QA System")

app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded"}
    )

app.include_router(router)
