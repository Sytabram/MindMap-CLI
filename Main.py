#!/usr/bin/env python3
"""
MindMap CLI - Command-line interface for managing mind maps (interactive only)
"""

# Import the CLI class that handles the interactive logic
from mindmap.cli import MindMapCLI

def main():
    # Create an instance of the CLI
    cli = MindMapCLI()
    # Start the CLI interaction loop
    cli.run()

# Entry point for the script when executed directly
if __name__ == "__main__":
    main()