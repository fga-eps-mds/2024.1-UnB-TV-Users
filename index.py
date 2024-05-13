import uvicorn
from dotenv import load_dotenv

load_dotenv()

from src.utils import dotenv

load_dotenv()
dotenv.validate_dotenv()

if __name__ == '__main__': # pragma: no cover
  port = 8000
  uvicorn.run('src.main:app', reload=True, port=int(port), host="0.0.0.0")