import metrics

class BKTreeNode():
    
    def __init__(self, key):
        self._key = key
        self._children = {}

class BKTree():
    
    def __init__(self, distance_function):
        self._root = None
        self._count = 0
        self._distance_function = metrics.levenshtein_distance_recursive
        
    def __len__(self):
        return self._count
        
    def insert(self, key):
        key = BKTreeNode(key)
        if self._root == None:
            self._root = key
            return
        current_node = self._root
        distance = self._distance_function(key._key, current_node)
        boolean = True
        while boolean == True:
            change_current = False
            for i, values in current_node.children.items():
              if values == distance:
                  current_node = current_node.children[i]
                  distance = self._distance_function(key._key, current_node)
                  change_current = True
            if change_current == False:
                current_node.children[key._key] = self._distance_function(key._key)
                boolean = False
        self._count += 1
        return
                    
    def get(self, key, max_dist = 1):
        """complete this function"""
        pass
    
