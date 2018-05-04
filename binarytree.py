class BinaryTreeNode():
    
    def __init__(self, key, value, left = None, right = None):
        self._key = key
        self._values = [value]
        self._left = None
        self._right = None
 

class BinaryTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count
        
    def insert(self, key, value):
        z = BinaryTreeNode(key, value)
        self._count += 1
        if self._root == None:
            self._root = z
            return
        if self.get(key) != None:
            self.get(key).append(value)
            return
        y = None
        x = self._root
        while x != None:
            y = x
            if key < x._key:
                x = x._left
            else:
                x = x._right
        if y == None:
            self._root = z
        elif z._key < y._key:
            y._left = z
        elif z._key > y._key:
            y._right = z
        return
    
                      
    def get(self, key):
        x = self._root
        if x._key == key:
            return x._values
        while x != None:
            if x._key == key:
                return x._values
            elif key < x._key:
                x = x._left
            else:
                x = x._right
        return None