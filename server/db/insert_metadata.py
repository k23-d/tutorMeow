from supabase_client import supabase

def insert_metadata(user_id: str, filename: str, path: str, timestamp: str):
    supabase.table("uploads").insert({
        "user_id": user_id,
        "filename": filename,
        "path": path,
        "uploaded_at": timestamp
    }).execute()
