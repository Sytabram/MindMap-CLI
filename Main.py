#!/usr/bin/env python3
"""
MindMap CLI - Command-line interface for managing mind maps
"""

from mindmap.models import Node

def main():
    """Main program entry point."""

    root = Node("My first map")

    child1 = root.add_child("Idea 1")
    child2 = root.add_child("Idea 2")

    child1.add_child("Subidea 1.1")
    child1.add_child("Subidea 1.2")
    child2.add_child("Subidea 2.1")

    print(f"Root node: {root.title}")
    print("Children:")
    for child in root.children:
        print(f"- {child.title}")
        for subchild in child.children:
            print(f"  - {subchild.title}")

if __name__ == "__main__":
    main()