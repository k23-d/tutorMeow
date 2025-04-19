from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from supabase_client import supabase
from datetime import datetime

app = FastAPI()

# Allow CORS from frontend (adjust URL as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your Vercel domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from production!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: str = Form(...)):
    file_bytes = await file.read()
    filename = file.filename
    timestamp = datetime.utcnow().isoformat()
    storage_path = f"{user_id}/{timestamp}_{filename}"

    # Upload file to Supabase Storage bucket
    supabase.storage.from_("uploads").upload(storage_path, file_bytes)

    # Insert metadata into Supabase DB
    supabase.table("uploads").insert({
        "user_id": user_id,
        "filename": filename,
        "path": storage_path,
        "uploaded_at": timestamp
    }).execute()

    return {"status": "success", "path": storage_path}

