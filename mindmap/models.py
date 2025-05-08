class Node:
    def __init__(self, title, parent=None):
        # Title of the node
        self.title = title
        # Reference to the parent node (None for root)
        self.parent = parent
        # List of child nodes
        self.children = []

    def add_child(self, title):
        """Create a new child node with the given title and attach it"""
        child = Node(title, self)
        self.children.append(child)
        return child
    
    def remove_child(self, node):
        """Remove a specific child node if it exists"""
        if node in self.children:
            self.children.remove(node)
            return True
        return False
    
    def get_level(self):
        """Calculate the depth level of this node (root is level 0)"""
        level = 0
        current = self
        while current.parent:
            level += 1
            current = current.parent
        return level
        
    def __str__(self):
        """Return the node title when printed"""
        return self.title
    
    def to_dict(self):
        """Convert the node and its children to a dictionary format (for saving)"""
        return {
            'title': self.title,
            'children': [child.to_dict() for child in self.children]
        }
    
    @staticmethod
    def from_dict(data, parent=None):
        """Reconstruct a node and its children from a dictionary (for loading)"""
        node = Node(data['title'], parent)
        for child_data in data.get('children', []):
            child = Node.from_dict(child_data, node)
            node.children.append(child)
        return node


class MindMap:
    def __init__(self, title, root_title=None):
        # Title of the mind map
        self.title = title
        # Create the root node (use custom title if provided)
        root_node_title = root_title if root_title is not None else title
        self.root = Node(root_node_title)
        
    def search_node(self, title, node=None):
        """Search for a node by title recursively (case-insensitive)"""
        if node is None:
            node = self.root

        # Match current node
        if node.title.lower() == title.lower():
            return node
        
        # Search recursively through children
        for child in node.children:
            result = self.search_node(title, child)
            if result:
                return result
        
        return None
        
    def get_path(self, node):
        """Return the path (titles) from the root to the specified node"""
        path = []
        current = node
        while current:
            path.insert(0, current.title)
            current = current.parent
        return path
    
    def to_dict(self):
        """Convert the entire mind map to a dictionary for saving"""
        return {
            'title': self.title,
            'root_title': self.root.title,
            'children': [child.to_dict() for child in self.root.children]
        }
        
    @classmethod
    def from_dict(cls, data):
        """Reconstruct a MindMap instance from a dictionary (e.g., loaded from JSON)"""
        # Support for backward compatibility with or without root_title
        if 'root_title' in data:
            mindmap = cls(data['title'], data['root_title'])
        else:
            mindmap = cls(data['title'])  # fallback
        
        # Rebuild the children recursively under the root node
        for child_data in data.get('children', []):
            child = Node.from_dict(child_data, mindmap.root)
            mindmap.root.children.append(child)
        
        return mindmap