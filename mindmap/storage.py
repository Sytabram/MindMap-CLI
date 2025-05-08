import json
import os
from .models import MindMap

class Storage:
    """
    Manages the saving and loading of mind maps from files
    """
    def __init__(self, data_dir="data"):
        # Directory where mind maps will be stored
        self.data_dir = data_dir
        # Create the directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
    def _get_full_path(self, filename):
        """
        Generate the full file path for a given filename,
        ensuring it ends with .json
        """
        if not filename.endswith('.json'):
            filename += '.json'
        return os.path.join(self.data_dir, filename)
        
    def save(self, mindmap, filename):
        """
        Save a MindMap instance to a JSON file
        """
        try:
            path = self._get_full_path(filename)
            data = mindmap.to_dict()  # Convert the MindMap to a dictionary
            
            # Write the data to file in JSON format
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            return True  # Successfully saved
        except Exception as e:
            # Print any error that occurred during saving
            print(f"Save error: {e}")
            return False
            
    def load(self, filename):
        """
        Load a MindMap instance from a JSON file
        """
        try:
            path = self._get_full_path(filename)
            
            # Read and parse the JSON file
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            return MindMap.from_dict(data)  # Reconstruct the MindMap
        except FileNotFoundError:
            # File does not exist
            print(f"File '{filename}' not found")
            return None
        except Exception as e:
            # Handle other loading errors
            print(f"Loading error: {e}")
            return None
            
    def list_files(self):
        """
        List all mind map filenames (without .json extension) in the data directory
        """
        files = []
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                files.append(filename[:-5])  # Strip the .json extension
        return files