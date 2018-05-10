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
        key = BKTreeNode(key)
        if self._root == None:
            self._root = key
            return
        current_node = self._root
        distance = self._distance_function(key._key, current_node._key)
        boolean = True
        while boolean == True:
            change_current = False
            for i, values in current_node._children.items():
                if values == distance:
                  current_node = current_node._children[distance]
                  distance = self._distance_function(values._key, current_node._key)
                  change_current = True
            if change_current == False:
                current_node._children[distance] = key
                boolean = False
        self._count += 1
        return
                    
    def get(self, key, max_dist = 1, current_node = 0):
        if current_node == 0:
            current_node = self._root
        results = []
        distance = self._distance_function(key, current_node._key)
        if distance <= max_dist:
            results.append(current_node._key, k)
        for k, value in current_node._children.items():
            if k <= distance + max_dist and k >=  distance - max_dist:
                results.append((current_node._children[k]._key, k))
                results.append(self.get(key, max_dist, current_node._children[k]))
        return results
