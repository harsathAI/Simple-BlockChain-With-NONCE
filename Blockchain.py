#Module to Use Time
import datetime
#Module to Use Hashing Algorithms and Generate Hashes
import hashlib

#This Class is for Creating a Block in our Block Chain
class Block:
    #Declaring All of Our Block Chain Related Variable
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    #Our Hash is a Haxa Decimal Data so we are declaring it as 0x0
    previous_hash = 0x0
    #Since this is not Needed but it Helps with the Time Data of the Block when Created
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        #We are Using SHA256 Algorithm(For Better Usage)
        h = hashlib.sha256()
        #We have to Encode it in utf-8 Format(for Hash Computational Process)

        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        #When Creating a New Block we Should Consider the Hash of the  Previous Block
        #Which is the Main Idea of Using BlockChain System
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()
        #Here we are Printing the Output of our Block
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20
    #The Maximum Value you can Store in a 32-BIT System
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    head = block

    #This Method will add a New Block to Our Block Chain Network
    def add(self, block):
        #In These Lines we are Updating Our Variables for the Next Iteration
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

        #This is a Cool Function which will iterate Till it finds a Desire Hash for the Block
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                #Updates the Nounce if it does not Finds one
                block.nonce += 1

blockchain = Blockchain()

#Here we are Adding 10 Blocks to Our Block Chain
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
