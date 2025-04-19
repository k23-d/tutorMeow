import uvicorn
import os
import sys

sys.path.append(os.path.dirname(__file__))

print("✅ Starting Uvicorn…")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"⚙️ Launching app on port {port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False, log_level="debug")
