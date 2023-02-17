"""
    blockchain class    
"""
from block import Block
import logging

class Blockchain:
    def __init__(self) -> None:
        self.name = "MEchain"
        self.head_block:Block  = None
    
    def __repr__(self) -> str:
        result = ''
        block = self.head_block
        while block:
            result = repr(block) + '\n'
            block = block.next_block
        return result