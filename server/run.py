import uvicorn
import os
import sys

sys.path.append(os.path.dirname(__file__))  # Ensure current folder in path

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
