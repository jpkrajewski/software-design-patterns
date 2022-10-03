from abc import ABC, abstractmethod


class Iterator(ABC):
    """Provide a way to access the elements of an aggregate object sequentially
    without exposing its underlying representation"""
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...


class BinaryTreeIterator(Iterator):
    def __init__(self, root):
        self.root = root
        self.array = self._traversal(root)

    def _traversal(self) -> list:
        ...

    def __iter__(self):
        self.array_len = len(self.array)
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.array_len:
            self.i += 1
            return self.array[self.i - 1]
        raise StopIteration


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        ...


class BinaryTree(Aggregate):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def create_iterator(self, traversal_strategy) -> Iterator:
        """New traversal operations should be defined for an aggregate object
         without changing its interface"""
        return traversal_strategy(self)


class InOrderIterator(BinaryTreeIterator):
    """In this traversal method, the left subtree is visited first, then the root and later the right sub-tree.
    We should always remember that every node may represent a subtree itself."""
    def _traversal(self, root):
        array = []
        if root:
            array = self._traversal(root.left)
            array.append(root.data)
            array = array + self._traversal(root.right)
        return array


class PreOrderIterator(BinaryTreeIterator):
    """In this traversal method, the root node is visited first,
    then the left subtree and finally the right subtree."""
    def _traversal(self, root):
        array = []
        if root:
            array.append(root.data)
            array = array + self._traversal(root.left)
            array = array + self._traversal(root.right)
        return array


class PostOrderIterator(BinaryTreeIterator):
    """In this traversal method, the root node is visited last, hence the name.
    First we traverse the left subtree, then the right subtree and finally the root node."""
    def _traversal(self, root):
        array = []
        if root:
            array = self._traversal(root.left)
            array = array + self._traversal(root.right)
            array.append(root.data)
        return array


btree = BinaryTree(27)
btree.insert(14)
btree.insert(35)
btree.insert(10)
btree.insert(19)
btree.insert(31)
btree.insert(42)

for node in btree.create_iterator(InOrderIterator):
    print(node)

for node in btree.create_iterator(PreOrderIterator):
    print(node)

for node in btree.create_iterator(PostOrderIterator):
    print(node)

