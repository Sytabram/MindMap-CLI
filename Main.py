#!/usr/bin/env python3
"""
MindMap CLI - Command-line interface for managing mind maps
"""

from mindmap.models import MindMap

def display_node(node, indent=0):
    """Recursively displays a node and its descendants"""
    print("  " * indent + "- " + node.title)
    for child in node.children:
        display_node(child, indent + 1)

def main():
    """Point d'entrée principal du programme"""

    mindmap = MindMap("My Project")
    print(f"Map created: {mindmap.title}")
    
    root = mindmap.root
    
    features = root.add_child("Features")
    tasks = root.add_child("Tasks")
    

    ui = features.add_child("User Interface")
    api = features.add_child("API")
    
    ui.add_child("Responsive design")
    
    print("\nMap structure:")
    display_node(root)
    
    search_for = "Responsive design"
    found = mindmap.find_node(search_for)
    if found:
        path = mindmap.get_path(found)
        print(f"\nPath for '{search_for}': {' > '.join(path)}")
        print(f"Level: {found.get_level()}")
    else:
        print(f"\nNode '{search_for}' Not Found")
    
    print("\nDeleting the 'API' node...")
    node_to_remove = mindmap.find_node("API")
    if node_to_remove and node_to_remove.parent:
        node_to_remove.parent.remove_child(node_to_remove)
        print("Node deleted")
    
    print("\nStructure after deletion:")
    display_node(root)

if __name__ == "__main__":
    main()