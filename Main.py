#!/usr/bin/env python3
"""
MindMap CLI - Command-line interface for managing mind maps (interactive only)
"""

from mindmap.cli import MindMapCLI

def main():
    cli = MindMapCLI()
    cli.run()

if __name__ == "__main__":
    main()