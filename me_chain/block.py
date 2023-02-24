"""
    blockchian block class    
"""

class Block:
    def __init__(self, index: int, timestamp: str, proof: int, prev_hash: str) -> None:
        #self.nonce = 0
        self.index = index
        self.proof = proof
        self.timestamp = timestamp
        self.prev_hash = prev_hash
    
    def __repr__(self) -> str:
        return f"Block(index={self.index}, timestamp={self.timestamp}, proof={self.proof}, prev_hash={self.prev_hash})"
    
    def json(self):
        return {"index": self.index, "timestamp": self.timestamp, "proof": self.proof, "prev_hash": self.prev_hash}