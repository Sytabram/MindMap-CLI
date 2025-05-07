class Node:
    def __init__(self, title, parent=None):
        self.title = title
        self.parent = parent
        self.children = []

    def add_child(self, title):
        child = Node(title, self)
        self.children.append(child)
        return child
    
    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)
            return True
        return False
    
    def get_level(self):
        level = 0
        current = self
        while current.parent:
            level += 1
            current = current.parent
        return level
        
    def __str__(self):
        return self.title
    
class MindMap:
 
    def __init__(self, title):
        self.root = Node(title)
        self.title = title
        
    def find_node(self, title, node=None):
        if node is None:
            node = self.root
            
        if node.title.lower() == title.lower():
            return node
            
        for child in node.children:
            result = self.find_node(title, child)
            if result:
                return result
                
        return None
        
    def get_path(self, node):
        path = []
        current = node
        while current:
            path.insert(0, current.title)
            current = current.parent
        return path