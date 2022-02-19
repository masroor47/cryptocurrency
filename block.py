from datetime import datetime

class Block:

    def __init__(self, transactions, previous_hash, nonce = 0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()
        