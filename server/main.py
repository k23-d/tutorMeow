from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from validators.pdf_text import extract_pdf_text
from validators.ai_validator import validate_pdf_with_ai
from storage.upload_file import upload_to_supabase
from db.insert_metadata import insert_metadata
from datetime import datetime
from fastapi.responses import JSONResponse
import os
import uvicorn 


print("✅ FastAPI app loading...")  # log to check app

app = FastAPI()

# Allow CORS from frontend (adjust URL as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to Vercel domain in prod
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
        if file.content_type != "application/pdf":
            return JSONResponse(status_code=400, content={"error": "Only PDFs are allowed."})
    
        file_bytes = await file.read()
        extracted_text = extract_pdf_text(file_bytes)
        is_valid = validate_pdf_with_ai(extracted_text)
    
        if not is_valid:
            return JSONResponse(status_code=400, content={"error": "File is not syllabus content."})
        
        timestamp = datetime.utcnow().isoformat()
        filename = file.filename
        storage_path = f"{user_id}/{timestamp}_{filename}"
        
        upload_to_supabase(storage_path, file_bytes)
        insert_metadata(user_id, filename, storage_path, timestamp)
    
        return {"status": "success", "path": storage_path}
        
    except Exception as e:
        print(f"❌ Upload failed: {str(e)}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    print("🔥 Finally working da...")
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
