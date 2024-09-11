---

# File Organizer

**File Organizer** is a command-line tool designed to help you organize files into directories based on their type or creation date. It also supports undoing previous operations and logs actions for easy restoration.

## Features

- **Organize Files by Type**: Move files into directories named after their file extensions.
- **Organize Files by Date**: Move files into directories based on their creation date (year and month).
- **Undo Operations**: Restore files to their original locations by undoing previous operations.
- **Log Operations**: Keeps a log of all operations performed for easy tracking and undoing.

## Installation

You can install the File Organizer tool via PyPI. To install, run:

```bash
pip install fileOrganizer
```

## Usage

The tool provides various commands and flags to manage your files:

### Organize Files

To organize files by type or date:

```bash
organize --path /your/directory --sort-by type
```

Or

```bash
organize --path /your/directory --sort-by date
```

### Undo Operations

To undo all previous file organization operations:

```bash
organize --path path_of_file --undo
```

This will revert the files back to their original locations and remove empty directories that were created during the organization process.

### Dry Run Mode

If you want to test the organization without making any changes, use the `--dry-run` flag:

```bash
organize --path /your/directory --sort-by type --dry-run
```

This will show you the moves that would be made without actually performing them.

## Flags

- `--path`: Specify the directory to organize.
- `--sort-by`: Choose between `type` or `date` to sort files by their file type or creation date.
- `--dry-run`: Run the command without making any changes (for preview purposes).
- `--undo`: Revert all previous operations and restore files to their original locations.

---
