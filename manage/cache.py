import os
import shutil  # Import shutil to use rmtree


def delete_pycaches():
    """Delete all __pycache__ directories in the current directory and subdirectories."""
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            print(f"Deleting {pycache_path}")
            # Remove the __pycache__ directory and its contents
            shutil.rmtree(pycache_path)
