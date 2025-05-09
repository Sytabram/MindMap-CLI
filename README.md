# MindMap CLI

MindMap CLI is a simple and interactive command-line tool for creating, editing, and saving hierarchical **mind maps** locally as `.json` files.

## 🚀 Features
```
Here are the available commands:

	•	create <title> – Create a new mind map with the given title

	•	load <filename> – Load an existing mind map from the data/ directory

	•	save [filename] – Save the current mind map (optionally under a new name)

	•	list – List all saved mind maps

	•	add <parent> – Add a new node under the specified parent node

	•	delete <title> – Delete a node by its title (root node cannot be deleted)

	•	display – Display the structure of the current mind map

	•	info – Show statistics (total nodes and max depth) for the current map

	•	search <title> – Search for a node by its title and display its path

	•	help – Show the list of commands and usage hints

	•	exit – Exit the program
```

## 📦 Installation

```bash
git clone https://github.com/Sytabram/MindMap-CLI  # Clone project
cd mindmap-cli                                     # Navigate into the project directory
python main.py                                     # Run 
```

## CLI Example
```
MindMap CLI - Type 'help' for available commands

mindmap> create My Project
Use custom root node title? (default: 'My Project') [y/N]: n
Created new mind map: 'My Project'

mindmap> add My Project
Using 'My Project' as parent node
Enter new node title: First Idea
Added 'First Idea' under 'My Project'

mindmap> add First Idea
Using 'First Idea' as parent node
Enter new node title: Sub Idea
Added 'Sub Idea' under 'First Idea'

mindmap> display

Map structure:
- My Project
  - First Idea
    - Sub Idea

mindmap> info

Mind Map: My Project
Root Node: My Project
Nodes: 3
Maximum depth: 2

mindmap> save
Map saved as 'My_Project.json'

mindmap> exit
Goodbye !
```
## 📁 File Structure
```
mindmap-cli/
├── main.py                     # Application entry point
├── mindmap/
│   ├── __init__.py
│   ├── models.py               # Data models (Node, MindMap)
│   ├── manager.py              # Managing map operations
│   ├── storage.py              # Saving/loading maps
│   └── cli.py                  # Command line interface management
├── data/                       # Folder for storing map files
└── README.md                   # Documentation
```

