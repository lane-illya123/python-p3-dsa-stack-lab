class Stack:

    def __init__(self, items = [], limit = 100):
        #if items is None:
        #    items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        
        return len(self.items) == 0

    def empty(self):
        
        return self.isEmpty()

    
    def push(self, item):
        if  not self.full():
            self.items.append(item)
        
            return self


    def pop(self):
        
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None   

    def peek(self):
        
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
        
    
    def size(self):
        
        return len(self.items)
        
    def full(self):
        
        return self.size() == self.limit

    def search(self, target):
        # Iterate through the stack starting from the top
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
            # Return the distance from the top to the matched element
                return len(self.items) - i - 1
    # If target element is not found, return -1
        return -1