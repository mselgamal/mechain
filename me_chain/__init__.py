from blockchain import Blockchain
from fastapi import FastAPI

app = FastAPI()
blockchain_service = Blockchain()

@app.get('/')
def homepage():
    return {"message": f"welcome to {blockchain_service.name}"}