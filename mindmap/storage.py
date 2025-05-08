import json
import os
from .models import MindMap

class Storage:
    """
    Manages the saving and loading of mind maps from files
    """
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
    def _get_full_path(self, filename):
        if not filename.endswith('.json'):
            filename += '.json'
        return os.path.join(self.data_dir, filename)
        
    def save(self, mindmap, filename):
        try:
            path = self._get_full_path(filename)
            data = mindmap.to_dict()
            
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            return True
        except Exception as e:
            print(f"Save error: {e}")
            return False
            
    def load(self, filename):
        try:
            path = self._get_full_path(filename)
            
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            return MindMap.from_dict(data)
        except FileNotFoundError:
            print(f"File '{filename}' not found")
            return None
        except Exception as e:
            print(f"Loading error: {e}")
            return None
            
    def list_files(self):
        files = []
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                files.append(filename[:-5])  # Remove .json extension
        return files