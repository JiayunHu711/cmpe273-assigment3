from bitarray import bitarray
import mmh3

class BloomFilter():
    def __init__(self, num_keys, false_pos_probablity):
        self.array = bitarray(num_keys)
        self.size = num_keys
        self.count = int(false_pos_probablity * 100)


    def add(self, item):
        for i in range (self.count):
            index = mmh3.hash(item, i) % self.size
            self.array[index] = 1
 
        return self
 
    def is_member(self, item):

        for i in range (self.count):
            index = mmh3.hash(item, i) % self.size
            if self.array[index] == 0:
                 return False
 
        return True