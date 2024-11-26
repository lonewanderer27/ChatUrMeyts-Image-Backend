from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.image import router as img_router
import logging
import os
import uvicorn

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chaturmeytsimg = FastAPI(
    title="Chat-Ur-Meyts Image API",
    description="API for Chat-Ur-Meyts Image",
    version="1.0"
)

chaturmeytsimg.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost", "http://localhost:5173", "https://chat-ur-meyts.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"]
)

chaturmeytsimg.include_router(img_router)

@chaturmeytsimg.get("/", tags=["Root"])
async def root():
    return {"message": "Hello klasmeyts! This is the root of the Chat-Ur-Meyts Image API."}

if __name__ == "__main__":
    uvicorn.run(chaturmeytsimg, host="0.0.0.0", port=int(
        os.environ.get("PORT", 8000)))