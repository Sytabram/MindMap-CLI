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
        # Initialize the mind map manager
        self.manager = MindMapManager()
        # Map of command names to their handler methods
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
        """Run the CLI application loop"""
        print("MindMap CLI - Type 'help' for available commands")
        
        while True:
            try:
                # Get user input
                command = input("\nmindmap> ").strip()
                
                if not command:
                    continue
                
                # Split into command and arguments
                parts = command.split(maxsplit=1)
                cmd = parts[0].lower()
                args = parts[1].split() if len(parts) > 1 else []
                
                # Execute the command if recognized
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
        """Create a new mind map with interactive prompts for title and root node"""
        if args:
            # Use provided arguments as the map title
            map_title = " ".join(args)
        else:
            # Ask the user for the map title
            map_title = input("Enter mind map title: ").strip()
            if not map_title:
                print("Map title cannot be empty")
                return
        
        # Ask the user if they want a custom root node title
        use_custom_root = input(f"Use custom root node title? (default: '{map_title}') [y/N]: ").strip().lower()
        
        root_title = None
        if use_custom_root and use_custom_root[0] == 'y':
            root_title = input("Enter root node title: ").strip()
            if not root_title:
                print("Using map title as root node title")
                root_title = None
        
        # Call the manager to create the map
        self.manager.create_map(map_title, root_title)
        
        if root_title:
            print(f"Created new mind map: '{map_title}' with root node: '{root_title}'")
        else:
            print(f"Created new mind map: '{map_title}'")
        
    def load_map(self, args):
        """Load an existing mind map from file"""
        if not args:
            print("Usage: load <filename>")
            return
            
        filename = args[0]
        success, message = self.manager.load_map(filename)
        print(message)
        
    def save_map(self, args):
        """Save the current mind map to file"""
        filename = args[0] if args else None
        success, message = self.manager.save_map(filename)
        print(message)
        
    def list_maps(self, args):
        """List all saved mind maps"""
        files = self.manager.list_maps()
        if not files:
            print("No mind maps found")
            return
            
        print("Available mind maps:")
        for file in files:
            print(f"- {file}")
            
    def display_map(self, args):
        """Print the structure of the current mind map"""
        output = self.manager.display_map()
        print("\nMap structure:")
        print(output)
        
    def add_node(self, args):
        """Add a new node to the current mind map"""
        if not self.manager.current_map:
            print("No active mind map. Create or load a map first.")
            return
            
        # Get the parent node title
        if args:
            parent = " ".join(args)
            print(f"Using '{parent}' as parent node")
        else:
            parent = input("Enter parent node title (or 'root'): ").strip()
            if not parent:
                print("Parent node cannot be empty")
                return
                
        # Get the new node title
        title = input("Enter new node title: ").strip()
        if not title:
            print("Node title cannot be empty")
            return
            
        success, message = self.manager.add_node(parent, title)
        print(message)
        
    def delete_node(self, args):
        """Delete a node from the current mind map"""
        if not self.manager.current_map:
            print("No active mind map. Create or load a map first.")
            return
            
        # Get the node title to delete
        if args:
            title = " ".join(args)
            print(f"Attempting to delete node '{title}'")
        else:
            title = input("Enter the title of the node to delete: ").strip()
            if not title:
                print("Node title cannot be empty")
                return
                
        # Confirm with the user before deleting
        confirm = input(f"Are you sure you want to delete '{title}'? [y/N]: ").strip().lower()
        if not confirm or confirm[0] != 'y':
            print("Deletion cancelled")
            return
            
        success, message = self.manager.delete_node(title)
        print(message)
        
    def search_node(self, args):
        """Search for a node by title"""
        if not self.manager.current_map:
            print("No active mind map. Create or load a map first.")
            return
            
        # Get the node title to search
        if args:
            title = " ".join(args)
            print(f"Searching for node '{title}'")
        else:
            title = input("Enter the title of the node to search: ").strip()
            if not title:
                print("Node title cannot be empty")
                return
                
        node = self.manager.search_node(title)
        
        if node:
            # Display node path and level
            path = self.manager.current_map.get_path(node)
            print(f"\nNode '{title}' found")
            print(f"Path: {' > '.join(path)}")
            print(f"Level: {node.get_level()}")
        else:
            print(f"Node '{title}' not found")
            
    def show_info(self, args):
        """Show basic statistics about the current mind map"""
        info = self.manager.get_map_info()
        if isinstance(info, str):
            print(info)
            return
            
        print(f"\nMind Map: {info['title']}")
        print(f"Root Node: {info['root_node']}")
        print(f"Nodes: {info['nodes']}")
        print(f"Maximum depth: {info['max_depth']}")
        
    def exit_app(self, args):
        """Exit the CLI application"""
        print("Goodbye !")
        sys.exit(0)
        
    def show_help(self, args):
        """Show a list of available commands"""
        print("\nAvailable commands:")
        print("  create [map_title]               - Create a new mind map (interactive prompts for details)")
        print("  load <filename>                  - Load an existing mind map")
        print("  save [filename]                  - Save the current mind map")
        print("  list                             - List all available mind maps")
        print("  display                          - Display the current mind map")
        print("  add [parent]                     - Add a new node (interactive prompts)")
        print("  delete [node_title]              - Delete a node (interactive prompts)")
        print("  search [node_title]              - Search a node (interactive prompts)")
        print("  info                             - Show information about the current map")
        print("  help                             - Show this help message")
        print("  exit                             - Exit the application")