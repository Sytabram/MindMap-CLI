#!/usr/bin/env python3
"""
MindMap CLI - Command-line interface for managing mind maps
"""

from mindmap.models import MindMap
from mindmap.storage import Storage


def display_node(node, indent=0):
    print("  " * indent + "- " + node.title)
    for child in node.children:
        display_node(child, indent + 1)

def main():

    storage = Storage()

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
    
    filename = "My_Project"
    if storage.save(mindmap, filename):
        print(f"\nMap saved in '{filename}.json'")
    
    print("\nLoading map from file...")
    loaded_map = storage.load(filename)
    if loaded_map:
        print(f"Map '{loaded_map.title}' successfully loaded")
        
        print("\nLoaded card structure:")
        display_node(loaded_map.root)
        
        search_for = "User Interface"
        found = loaded_map.find_node(search_for)
        if found:
            path = loaded_map.get_path(found)
            print(f"\nNode '{search_for}' Found")
            print(f"Path: {' > '.join(path)}")
            print(f"Level: {found.get_level()}")
    
    print("\nMind maps available:")
    for file in storage.list_files():
        print(f"- {file}")

if __name__ == "__main__":
    main()