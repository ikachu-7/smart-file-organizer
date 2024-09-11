# Smart File Organizer

**Smart File Organizer** is a command-line tool designed to help you organize files into directories based on their type or creation date. It also supports undoing previous operations and logs actions for easy restoration.

## Features

- **Organize Files by Type**: Move files into directories named after their file extensions.
- **Organize Files by Date**: Move files into directories based on their creation date (year and month).
- **Undo Operations**: Restore files to their original locations by undoing previous operations.
- **Log Operations**: Keeps a log of all operations performed for easy tracking and undoing.

## Installation

You can install the File Organizer tool via PyPI. To install, run:

```bash
pip install SmartFileOrganizer
```

## Usage

The tool provides various commands and flags to manage your files:

### Organize Files by Type

To organize files by type, use:

```bash
organize --path /your/directory --by type
```

This command will move files into directories named after their file extensions.

### Organize Files by Date

To organize files by creation date, use:

```bash
organize --path /your/directory --by date
```

This command will move files into directories based on their creation date (year and month).

### Undo Operations

To undo all previous file organization operations, use:

```bash
organize --path /your/directory --undo
```

This command will revert the files to their original locations and remove empty directories that were created during the organization process.

### Dry Run Mode

To preview the organization process without making any changes, use the `--dry-run` flag:

```bash
organize --path /your/directory --by type --dry-run
```

This command will show you the moves that would be made without actually performing them.

## Available Flags

- `--path`: Specify the directory to organize.
- `--by`: Choose between `type` or `date` to sort files by their file type or creation date.
- `--dry-run`: Run the command without making any changes (for preview purposes).
- `--undo`: Revert all previous operations and restore files to their original locations.
```
