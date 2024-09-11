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

def _log_operation(operation):
    """Log the operation to a file for undo purposes."""
    log_file_path = get_log_file_path()

    # Create the log file if it does not exist
    if not log_file_path.exists():
        log_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file_path, 'w') as f:
            json.dump([], f, indent=4)
        set_file_permissions(log_file_path)
    
    # Read the existing log file
    with open(log_file_path, 'r') as f:
        log = json.load(f)

    log.append(operation)
    
    # Write the updated log file
    with open(log_file_path, 'w') as f:
        json.dump(log, f, indent=4)

    # Ensure log file permissions are set
    set_file_permissions(log_file_path)

def organize_files(path, sort_by, dry_run):
    path_obj = Path(path)
    
    if not path_obj.exists():
        print(f"Error: The path {path} does not exist.")
        return

    for item in path_obj.iterdir():
        if item.is_file():
            if sort_by == 'type':
                _organize_by_type(item, dry_run, sort_by)
            elif sort_by == 'date':
                _organize_by_date(item, dry_run, sort_by)

def _organize_by_type(file, dry_run, method):
    file_extension = file.suffix[1:] 
    new_folder = file.parent / file_extension.upper()
    
    if dry_run:
        print(f"Would move {file} to {new_folder}")
    else:
        new_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(new_folder / file.name))
        _log_operation({
            'action': 'move',
            'file': str(file),
            'oldpath': str(file),
            'newpath': str(new_folder / file.name),
            'method': method
        })
        print(f"Moved {file} to {new_folder}")

def _organize_by_date(file, dry_run, method):
    import time
    file_creation_time = file.stat().st_ctime
    creation_year = Path(time.strftime('%Y', time.gmtime(file_creation_time)))
    creation_month = Path(time.strftime('%B', time.gmtime(file_creation_time)))
    
    new_folder = file.parent / creation_year / creation_month
    
    if dry_run:
        print(f"Would move {file} to {new_folder}")
    else:
        new_folder.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(new_folder / file.name))
        _log_operation({
            'action': 'move',
            'file': str(file),
            'oldpath': str(file),
            'newpath': str(new_folder / file.name),
            'method': method
        })
        print(f"Moved {file} to {new_folder}")
