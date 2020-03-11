class DynamicArray:
    def __init__(self, capcity):
        self.capacity = capcity
        self.count = 0
        self.storage = [None] * self.capacity
    def insert(self, index, value):
        