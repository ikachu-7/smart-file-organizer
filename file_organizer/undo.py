import json
import shutil
import os
from pathlib import Path

LOG_FILE = 'organizer_log.json'

def get_log_file_path():
    """Get the path to the log file within the package."""
    log_file_path = Path('file_organizer') / 'data' / LOG_FILE
    return log_file_path

def set_file_permissions(file_path):
    """Set file permissions to restrict access."""
    # Set the permissions to 600 (read and write for owner only)
    os.chmod(file_path, 0o600)

def remove_empty_dirs(dir_path):
    """Recursively remove empty directories."""
    for subdir in sorted(dir_path.iterdir(), reverse=True):
        if subdir.is_dir():
            remove_empty_dirs(subdir)
            try:
                if not any(subdir.iterdir()):  # Check if directory is empty
                    subdir.rmdir()
                    print(f"Removed empty directory: {subdir}")
            except OSError as e:
                print(f"Error removing directory {subdir}: {e}")

def undo_all_operations():
    """Undo all operations logged in the log file and update the log file accordingly."""
    log_file_path = get_log_file_path()

    # Create the log file if it does not exist
    if not log_file_path.exists():
        print("No operations to undo.")
        return

    with open(log_file_path, 'r') as f:
        log = json.load(f)
    
    if not log:
        print("No operations to undo.")
        return

    updated_log = []
    dirs_to_remove = set()

    for operation in reversed(log):
        old_path = Path(operation['oldpath'])
        new_path = Path(operation['newpath'])
        method = operation.get('method', 'type')  # Default to 'type' if not specified

        # Move file from new_path to the parent directory of old_path
        if new_path.exists():
            target_path = old_path.parent / new_path.name
            shutil.move(str(new_path), str(target_path))
            print(f"Undid move: {new_path} restored to {target_path}")

            # Add directories to remove if they are empty
            dirs_to_remove.add(new_path.parent)

            # Update the log entry to reflect the new operation
            updated_log.append({
                'action': 'restore',
                'file': str(target_path),
                'oldpath': str(target_path),
                'newpath': str(new_path),
                'method': method
            })
        else:
            print(f"Error: File {new_path} does not exist for undo.")
    
    # Remove empty directories created during the organization
    for dir_to_remove in sorted(dirs_to_remove, reverse=True):
        try:
            if dir_to_remove.is_dir() and not any(dir_to_remove.iterdir()):
                # Remove directory based on method
                if method == 'date':
                    parent_dir = dir_to_remove.parent
                    if not any(parent_dir.iterdir()):
                        parent_dir.rmdir()
                        print(f"Removed empty parent directory: {parent_dir}")
                dir_to_remove.rmdir()
                print(f"Removed empty directory: {dir_to_remove}")
        except OSError as e:
            print(f"Error removing directory {dir_to_remove}: {e}")
    
    # Final cleanup loop: Remove all empty directories in the current working directory
    root_dir = Path.cwd()  # Current working directory
    remove_empty_dirs(root_dir)

    # Clear and update the log file with the new state
    with open(log_file_path, 'w') as f:
        json.dump(updated_log, f, indent=4)
    
    # Set permissions for the log file
    set_file_permissions(log_file_path)

if __name__ == '__main__':
    undo_all_operations()
