"""
    blockchain class    
"""
from block import Block
import hashlib
import datetime
import json
import logging

class Blockchain:
    def __init__(self) -> None:
        self.name = "MEchain"
        self.chain:list[Block] = []
        self.create_block(proof=1, prev_hash='0')
    
    def create_block(self, proof: int, prev_hash: str):
        self.chain.append(Block(len(self.chain)+1, datetime.datetime.utcnow(), proof, prev_hash))
            
    def mine(self):
        pass
    
    def get_last_block(self):
        return self.chain[-1]
    
    def get_proof_of_work(self):
        pass
    
    def __repr__(self) -> str:
        result = ''
        block = self.head_block
        while block:
            result = repr(block) + '\n'
            block = block.next_block
        return result