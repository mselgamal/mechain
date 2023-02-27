from me_chain.blockchain import Blockchain
from fastapi import FastAPI

app = FastAPI()
blockchain_service = Blockchain()
app.state.mechain = blockchain_service

@app.get('/')
def homepage():
    return {"message": f"welcome to {app.state.mechain.name}"}

@app.get('/mine_block')
def mine_block():
    proof = blockchain_service.proof_of_work(blockchain_service.get_last_block().proof)
    blockchain_service.create_block(proof, blockchain_service.hash(blockchain_service.get_last_block()))
    return blockchain_service.get_last_block().json()

@app.get('/is_chain_valid')
def is_chain_valid():
    return {"is_valid": blockchain_service.is_chain_valid()}

@app.get('/get_chain')
def get_chain():
    return blockchain_service