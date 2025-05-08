"""
MindMap CLI - Command-line interface for interacting with mind maps
"""

import sys
from mindmap.manager import MindMapManager

class MindMapCLI:
    """
    Command-line interface for MindMap application
    """
    def __init__(self):
        self.manager = MindMapManager()
        self.commands = {
            'create': self.create_map,
            'load': self.load_map,
            'save': self.save_map,
            'list': self.list_maps,
            'display': self.display_map,
            'add': self.add_node,
            'delete': self.delete_node,
            'search': self.search_node,
            'info': self.show_info,
            'exit': self.exit_app,
            'help': self.show_help,
        }
        
    def run(self):
        """Run the CLI application"""
        print("MindMap CLI - Type 'help' for available commands")
        
        while True:
            try:
                command = input("\nmindmap> ").strip()
                
                if not command:
                    continue
                    
                parts = command.split()
                cmd = parts[0].lower()
                args = parts[1:]
                
                if cmd in self.commands:
                    self.commands[cmd](args)
                else:
                    print(f"Unknown command: '{cmd}'. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
                
    def create_map(self, args):
        """Create a new mind map"""
        if not args:
            print("Usage: create <map_title>")
            return
            
        title = " ".join(args)
        self.manager.create_map(title)
        print(f"Created new mind map: '{title}'")
        
    def load_map(self, args):
        """Open an existing mind map"""
        if not args:
            print("Usage: open <filename>")
            return
            
        filename = args[0]
        success, message = self.manager.load_map(filename)
        print(message)
        
    def save_map(self, args):
        """Save the current mind map"""
        filename = args[0] if args else None
        success, message = self.manager.save_map(filename)
        print(message)
        
    def list_maps(self, args):
        """List all available mind maps"""
        files = self.manager.list_maps()
        if not files:
            print("No mind maps found")
            return
            
        print("Available mind maps:")
        for file in files:
            print(f"- {file}")
            
    def display_map(self, args):
        """Display the structure of the current mind map"""
        output = self.manager.display_map()
        print("\nMap structure:")
        print(output)
        
    def add_node(self, args):
        """Add a new node to the mind map"""
        if len(args) < 2:
            print("Usage: add <parent_node> <node_title>")
            return
            
        parent = args[0]
        title = " ".join(args[1:])
        success, message = self.manager.add_node(parent, title)
        print(message)
        
    def delete_node(self, args):
        """Delete a node from the mind map"""
        if not args:
            print("Usage: delete <node_title>")
            return
            
        title = " ".join(args)
        success, message = self.manager.delete_node(title)
        print(message)
        
    def search_node(self, args):
        """Search a node in the mind map"""
        if not args:
            print("Usage: search <node_title>")
            return
            
        title = " ".join(args)
        node = self.manager.search_node(title)
        
        if node:
            path = self.manager.current_map.get_path(node)
            print(f"\nNode '{title}' found")
            print(f"Path: {' > '.join(path)}")
            print(f"Level: {node.get_level()}")
        else:
            print(f"Node '{title}' not found")
            
    def show_info(self, args):
        """Show information about the current mind map"""
        info = self.manager.get_map_info()
        if isinstance(info, str):
            print(info)
            return
            
        print(f"\nMind Map: {info['title']}")
        print(f"Nodes: {info['nodes']}")
        print(f"Maximum depth: {info['max_depth']}")
        
    def exit_app(self, args):
        """Exit the application"""
        print("Goodbye !")
        sys.exit(0)
        
    def show_help(self, args):
        """Show help information"""
        print("\nAvailable commands:")
        print("  create <title>           - Create a new mind map")
        print("  load <filename>          - load an existing mind map")
        print("  save [filename]          - Save the current mind map")
        print("  list                     - List all available mind maps")
        print("  display                  - Display the current mind map")
        print("  add <parent> <title>     - Add a new node")
        print("  delete <title>           - Delete a node")
        print("  search <title>           - Search a node")
        print("  info                     - Show information about the current map")
        print("  help                     - Show this help message")
        print("  exit                     - Exit the application")