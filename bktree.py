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
            self._count += 1
            return
        current_node = self._root
        distance = self._distance_function(key._key, current_node._key)
        loop_condition = True
        while loop_condition == True:
            if distance in current_node._children.keys():
                current_node = current_node._children[distance]
                distance = self._distance_function(current_node._key, key._key)
            else:
                current_node._children[distance] = key
                loop_condition = False
        self._count += 1
        return
                    
    def get(self, key, max_dist = 1, current_node = 0, results = []):
        if current_node == 0:
            current_node = self._root
            if self._distance_function(current_node._key, key) <= max_dist:
                results.append((current_node._key, self._distance_function(current_node._key, key)))
        distance = self._distance_function(key, current_node._key)
        for k, value in current_node._children.items():
            if k <= distance + max_dist and k >=  distance - max_dist:
                if (self._distance_function(key, value._key)) <= max_dist:
                    distance = self._distance_function(key, value._key)
                    results.append((value._key, distance))
                    self.get(key, max_dist, value, results)
                else:
                    self.get(key, max_dist, value, results)
        return results
