"""
    blockchain class    
"""
from typing import List
from me_chain.block import Block
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
        self.chain.append(Block(len(self.chain)+1, str(datetime.datetime.utcnow()), proof, prev_hash))
            
    def mine(self):
        pass
    
    def get_last_block(self):
        return self.chain[-1]
    
    def __check_proof(self, new_proof, prev_proof):
        hash_operation = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            return True 
        return False
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            if self.__check_proof(new_proof, previous_proof):
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block: Block):
        encoded_block = json.dumps(block.json(), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self):
        prev_block: Block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block.prev_hash != self.hash(prev_block):
                return False
            if not self.__check_proof(block.proof, prev_block.proof):
                return False
            prev_block = block
            block_index += 1
            
        return True
    
    def __repr__(self) -> str:
        result = ''
        for i in range(len(self.chain)):
            result += repr(self.chain[i]) + '\n'
        return result