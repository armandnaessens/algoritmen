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
        y = self._nil
        x = self._root
        
        while(x != self._nil):
            y = x
            if key < x._key:
                x = x.left
            else:
                x = x._right
        """ verder af werken """
            
        
        pass
                            
    def _right_rotate(self, node):
        y = node._right
        node._left = y._right
        if y._right != self._nil:
            y._right._parent = node
        if node._parent == self._nil:
            self._root = y
        elif node == node._parent._right:
            node._parent._right = y
        else:
            node._parent._left = y
        y._left = node
        node._parent = y
        pass
        
    def _left_rotate(self, node):
        y = node._right
        node._right = y._left
        if y._left != self._nil:
            y._left._parent = node
        y._parent = x._parent
        if node._parent == self._nil:
            self._root = y
        elif node == node._parent._left:
            node._parent._left = y
        else:
            node._parent._right = y
        y._left = node
        node._parent = y
        pass
                    
    def get(self, key):
        return search(self._root, key)
        
    def search(x,k):
        if x == NIL || k == x._key:
            return x
        if k < x.key:
            return search(x._left,k)
        else:
            return search(x._right,k)