class BKTreeNode():
    
    def __init__(self, key):
        self._key = key
        self._children = {}

class BKTree():
    
    def __init__(self, distance_function):
        self._root = None
        self._count = 0
        self._distance_function = distance_function
        
    def __len__(self):
        return self._count
        
    def insert(self, key):
        """complete this function"""
        pass
                    
    def get(self, key, max_dist = 1):
        """complete this function"""
        pass