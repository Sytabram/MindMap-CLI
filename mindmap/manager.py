"""
MindMap Manager - Core logic for managing mind maps
"""

from mindmap.models import MindMap, Node
from mindmap.storage import Storage

class MindMapManager:
    """
    Manager class for handling mind map operations
    """
    def __init__(self, data_dir="data"):
        # Initialize the storage system (file-based persistence)
        self.storage = Storage(data_dir)
        # Holds the currently active mind map
        self.current_map = None
        
    def create_map(self, title, root_title=None):
        """Create a new mind map with a title and optional root node title"""
        self.current_map = MindMap(title, root_title)
        return self.current_map
        
    def save_map(self, filename=None):
        """Save the current mind map to file"""
        if not self.current_map:
            return False, "No active mind map to save"
        
        # Default filename is the map title with spaces replaced by underscores
        if not filename:
            filename = self.current_map.title.replace(" ", "_")
        
        success = self.storage.save(self.current_map, filename)
        if success:
            return True, f"Map saved as '{filename}.json'"
        return False, "Failed to save mind map"
        
    def load_map(self, filename):
        """Load a mind map from file"""
        loaded_map = self.storage.load(filename)
        if loaded_map:
            self.current_map = loaded_map
            return True, f"Loaded map: {loaded_map.title}"
        return False, f"Could not load map: {filename}"
        
    def list_maps(self):
        """List all available mind maps in the data directory"""
        return self.storage.list_files()
        
    def add_node(self, parent_title, node_title):
        """Add a node under the specified parent node"""
        if not self.current_map:
            return False, "No active mind map"
        
        # Handle special case if parent is 'root'
        if parent_title.lower() == "root" or parent_title.lower() == self.current_map.root.title.lower():
            parent = self.current_map.root
        else:
            parent = self.current_map.search_node(parent_title)
        
        if not parent:
            return False, f"Parent node '{parent_title}' not found"
        
        # Add the new child node
        new_node = parent.add_child(node_title)
        parent_display_title = self.current_map.root.title if parent == self.current_map.root else parent_title
        return True, f"Added '{node_title}' under '{parent_display_title}'"
        
    def delete_node(self, node_title):
        """Delete a node from the mind map"""
        if not self.current_map:
            return False, "No active mind map"
        
        node = self.current_map.search_node(node_title)
        if not node:
            return False, f"Node '{node_title}' not found"
        
        if node == self.current_map.root:
            return False, "Cannot delete the root node"
        
        parent = node.parent
        if parent.remove_child(node):
            return True, f"Deleted node '{node_title}'"
        return False, "Failed to delete node"
        
    def search_node(self, title):
        """Search for a node by its title"""
        if not self.current_map:
            return None
        
        # Shortcut for searching the root
        if title.lower() == "root":
            return self.current_map.root
        
        return self.current_map.search_node(title)
        
    def display_map(self, node=None, indent=0):
        """Return a formatted string representing the mind map hierarchy"""
        if not self.current_map:
            return "No active mind map"
        
        if node is None:
            node = self.current_map.root
        
        result = []
        result.append("  " * indent + "- " + node.title)
        for child in node.children:
            result.append(self.display_map(child, indent + 1))
        return "\n".join(result)
        
    def get_map_info(self):
        """Get basic stats about the current mind map"""
        if not self.current_map:
            return "No active mind map"
        
        node_count = self._count_nodes(self.current_map.root)
        max_depth = self._get_max_depth(self.current_map.root)
        
        return {
            "title": self.current_map.title,
            "root_node": self.current_map.root.title,
            "nodes": node_count,
            "max_depth": max_depth
        }
        
    def _count_nodes(self, node):
        """Recursively count nodes starting from the given node"""
        count = 1  # Include current node
        for child in node.children:
            count += self._count_nodes(child)
        return count
        
    def _get_max_depth(self, node, current_depth=0):
        """Recursively determine the maximum depth from the given node"""
        if not node.children:
            return current_depth
        
        max_child_depth = 0
        for child in node.children:
            depth = self._get_max_depth(child, current_depth + 1)
            max_child_depth = max(max_child_depth, depth)
        
        return max_child_depth