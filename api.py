
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI(
    title="Movie Recap Studio API",
    description="Backend API for Movie Recap Studio",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Movie Recap Studio Backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "ai_enabled": False,
        "message": "Backend test successful"
    }


@app.post("/generate-recap")
async def generate_recap(video: UploadFile = File(...)):
    allowed_types = {
        "video/mp4",
        "video/quicktime",
        "video/x-matroska",
        "video/x-msvideo",
        "video/webm",
    }

    if video.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Please upload a supported video file."
        )

    return {
        "status": "received",
        "filename": video.filename,
        "message": (
            "Video upload endpoint is working. "
            "AI recap processing is not enabled yet."
        )
    }
