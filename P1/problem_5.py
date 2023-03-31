

import datetime
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self._calc_hash()

    def get_hash(self):
        return self.hash

    def get_data(self):
        return self.data

    def __str__(self):
        return 'Timestamp: {} \nData: {} \nHash: {} \nPrevious hash: {}'.format(self.timestamp, self.data, self.hash, self.previous_hash)

    ## private method
    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8')
        hash_str += str(self.data).encode('utf-8')
        hash_str += str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()class Block:

    def __init__(self, timestamp, data, previous_hash = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self._calc_hash()

    def get_hash(self):
        return self.hash

    def get_data(self):
        return self.data

    def __str__(self):
        return 'Timestamp: {} \nData: {} \nHash: {} \nPrevious hash: {}'.format(self.timestamp, self.data, self.hash, self.previous_hash)

    ## private method
    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8')
        hash_str += str(self.data).encode('utf-8')
        hash_str += str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


# blocks
block_zero = Block(get_timestamp(), "Information X", 0)
block_one = Block(get_timestamp(), "Information Y", block_zero)
block_two = Block(get_timestamp(), "Information Z", block_one)

# linked list
linked_list = LinkedList()
linked_list.append(get_timestamp(), "Information A")
linked_list.append(get_timestamp(), "Information B")

# tests
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list last data : ", linked_list.last.data)
print("Linked list last's previous hash data : ", linked_list.last.previous_hash.data)
