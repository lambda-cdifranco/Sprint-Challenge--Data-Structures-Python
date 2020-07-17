class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.front = 0
        self.back = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.front] = item
            if self.front == len(self.storage) - 1:
                self.front = 0
            else:
                self.front += 1
            if self.back == len(self.storage) - 1:
                self.back = 0
            else:
                self.back += 1
        else:    
            self.storage.append(item)
            self.back += 1

    def get(self):
        return self.storage


buffer = RingBuffer(5)    
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')