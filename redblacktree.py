class RedBlackTreeNode():
    
    def __init__(self, key, value, parent = None, left = None, right = None):
        self._key = key
        self._values = [value]
        self._parent = parent
        self._black = False
        self._left = None
        self._right = None


class RedBlackTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count
        
    def insert(self, key, value):
        z = RedBlackTreeNode(key, value)
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
        z._parent = y
        if y == None:
            self._root = z
        elif z._key < y._key:
            y._left = z
        else: #elif z._key > y._key:  zou hier voor else gaan, == is toch al uitgesloten op lijn 27
            y._right = z
        z._left = None
        z.right = None
        z._black = False;
        self._RB_fix(z)
        return
    
    def _RB_fix(self, z): # _ voor de naam is conventie als het enkel binnen de klasse gebruikt wordt
        if z._parent._parent == None: # z._parent is root
            return
        while not z._parent._black:
            if z._parent == z._parent._parent._left:
                y = z._parent._parent._right
                if y == None:
                    y = RedBlackTreeNode(None, None)
                if not y._black:
                    z._parent._black = True
                    y._black = True
                    z._parent._parent._black = False
                elif z == z._parent._right:
                    z = z._parent
                    self._left_rotate(z)
                    z._parent._black = True
                    z._parent._parent._black = False
                    self._right_rotate(z._parent._parent)
            else:
                y = z._parent._parent._left
                if y == None:
                    y = RedBlackTreeNode(None, None)
                if not y._black:
                    z._parent._black = True
                    y._black = True
                    z._parent._parent._black = False
                elif z == z._parent._left:
                    z = z._parent
                    self._right_rotate(z)
                    z._parent._black = True
                    z._parent._parent._black = False
                    self._left_rotate(z._parent._parent)
        self._root._black = True
        return
                          
    def _right_rotate(self, node):
        y = node._left
        node._left = y._right
        if y._right != None:
            y._right._parent = node
        y._parent = node._parent
        if node._parent == None:
            self._root = y
        elif node == node._parent._right:
            node._parent._right = y
        else:
            node._parent._left = y
        y._right = node
        node._parent = y
        return
        
    def _left_rotate(self, node):
        y = node._right
        node._right = y._left
        if y._left != None:
            y._left._parent = node
        y._parent = node._parent
        if node._parent == None:
            self._root = y
        elif node == node._parent._left:
            node._parent._left = y
        else:
            node._parent._right = y
        y._left = node
        node._parent = y
        return
                    
    def get(self, key, current_node = 0):
        if current_node == 0:
            current_node = self._root
        if current_node == None:
            return None
        else:
            if current_node._key == key:
                return current_node
            if key < current_node._key:
                return self.get(key, current_node._left)
            else:
                return self.get(key, current_node._right)
    
    #    return search(self, key)
    #def search(self, key , current_node = self._root):
       # if x == None:
        #    return None
        #else: 
         #   if x._key in (NIL,k):
          #      return x._values
           # if k < x._key:
            #    return search(x._left,k)
            #else:
             #   return search(x._right,k)