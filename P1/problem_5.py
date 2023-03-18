import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, timestamp, data, previous_hash=0):
        new_node = Block(timestamp, data, previous_hash)
        if self.head is None:
            self.head = new_node
        else:
            new_node.previous_hash = self.head
            self.head = new_node
            


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%H:%M:%S")

first = Block(get_timestamp(), "Hello", 0)
second = Block(get_timestamp(), "World", first)
third = Block(get_timestamp(), "Start", second)

linked_list = LinkedList()
linked_list.append(first)
linked_list.append(second)