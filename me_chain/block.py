"""
    blockchian block class    
"""

class Block:
    def __init__(self) -> None:
        self.nonce = 0
        self.id = 0
        self.data = None
        self.hash = None
        self.prev_hash = None
        self.prev_block = None
        self.next_block = None