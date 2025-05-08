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
    
    def to_dict(self):
        return {
            'title': self.title,
            'children': [child.to_dict() for child in self.children]
        }
    
    @staticmethod
    def from_dict(data, parent=None):
        node = Node(data['title'], parent)
        for child_data in data.get('children', []):
            child = Node.from_dict(child_data, node)
            node.children.append(child)
        return node
        
class MindMap:
    def __init__(self, title, root_title=None):
        self.title = title
        root_node_title = root_title if root_title is not None else title
        self.root = Node(root_node_title)
        
    def search_node(self, title, node=None):
        if node is None:
            node = self.root
            
        if node.title.lower() == title.lower():
            return node
            
        for child in node.children:
            result = self.search_node(title, child)
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
    
    def to_dict(self):
        return {
            'title': self.title,
            'root_title': self.root.title,
            'children': [child.to_dict() for child in self.root.children]
        }
        
    @classmethod
    def from_dict(cls, data):
        # Check if the data contains a separate root_title
        if 'root_title' in data:
            mindmap = cls(data['title'], data['root_title'])
        else:
            # For backward compatibility with older saved maps
            mindmap = cls(data['title'])
            
        for child_data in data.get('children', []):
            child = Node.from_dict(child_data, mindmap.root)
            mindmap.root.children.append(child)
        return mindmap