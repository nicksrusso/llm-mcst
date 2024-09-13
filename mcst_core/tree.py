from utils import Node_Type


class Node():
    def __init__(self, depth, type, parent, children):
        self.depth = depth
        self.type = type
        self.parent = parent
        self.children = children
        self.uct = 0
        self.value = 0
        self.visits = 0
        
        
class TreeSearcher():
    """Searches the tree"""