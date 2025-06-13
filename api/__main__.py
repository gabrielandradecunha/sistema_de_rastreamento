import sys
import os
from dotenv import load_dotenv

load_dotenv()
app_port = os.getenv('APP_PORT')

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.main import app  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(app_port), reload=True)
