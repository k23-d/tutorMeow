from supabase_client import supabase

def upload_to_supabase(path: str, file_bytes: bytes):
    supabase.storage.from_("uploads").upload(path, file_bytes)
