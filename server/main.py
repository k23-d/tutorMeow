from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from supabase_client import supabase
from datetime import datetime
import os
import uvicorn 


print("✅ FastAPI app loading...")  # Add this at the top

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

@app.get("/test")
def roottest():
    return {"message": "THE SERVER IS UP"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: str = Form(...)):
    try:
        file_bytes = await file.read()
        filename = file.filename
        timestamp = datetime.utcnow().isoformat()
        storage_path = f"{user_id}/{timestamp}_{filename}"

        print(f"Uploading file: {filename} for user: {user_id}")
        print(f"Storage path: {storage_path}")

        # Upload to Supabase Storage
        storage_response = supabase.storage.from_("uploads").upload(storage_path, file_bytes)
        print(f"Storage upload response: {storage_response}")

        # Insert metadata into Supabase DB
        db_response = supabase.table("uploads").insert({
            "user_id": user_id,
            "filename": filename,
            "path": storage_path,
            "uploaded_at": timestamp
        }).execute()
        print(f"DB insert response: {db_response}")

        return {"status": "success", "path": storage_path}

    except Exception as e:
        print(f"❌ Upload failed: {str(e)}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    print("🔥 Finally working da...")
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
