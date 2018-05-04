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
        if y == None:
            self._root = z
        elif z._key < y._key:
            y._left = z
        elif z._key > y._key:
            y._right = z
        z._left = None
        z.right = None
        z._black = False;
        RB_fix(self,z)
        return
    
    def RB_fix(self, node):
        while not z._parent._black:
            if z._parent == z._parent._parent._left:
                y = z._parent._parent._right
                if not y._black:
                    z._parent._black = true
                    y._black = true
                    z._parent._parent._black = false
                elif z == z._parent._right:
                    z = z._parent
                    _left_rotate(self,z)
                    z._parent._black = true
                    z._parent._parent._black = false
                    _right_rotate(self,z._parent._parent)
            else:
                y = z._parent._parent._left
                if not y._black:
                    z._parent._black = true
                    y._black = true
                    z._parent._parent._black = false
                elif z == z._parent._left:
                    z = z._parent
                    _right_rotate(self,z)
                    z._parent._black = true
                    z._parent._parent._black = false
                    _left_rotate(self,z._parent._parent)
        self._root._black = true
        return
                          
    def _right_rotate(self, node):
        y = node._right
        node._left = y._right
        if y._right != None:
            y._right._parent = node
        if node._parent == None:
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
        if x == None:
            return None
        else: 
            if x._key in (NIL,k):
                return x._values
            if k < x._key:
                return search(x._left,k)
            else:
                return search(x._right,k)