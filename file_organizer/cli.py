import click
from file_organizer.organizer import organize_files
from file_organizer.undo import undo_all_operations

@click.command()
@click.option('--path', required=True, help='Path to the directory to organize.')
@click.option('--by', default='type', help='Organize files by "type" or "date".')
@click.option('--dry-run', is_flag=True, help='Preview changes without making them.')
@click.option('--undo', is_flag=True, help='Undo all file organization operations.')
def cli(path, by, dry_run, undo):
    """
    CLI tool to organize files in a specified directory by file type or date.
    """
    if undo:
        undo_all_operations()
    else:
        click.echo(f"Organizing files in: {path}")
        click.echo(f"Sorting by: {by}")
        
        if dry_run:
            click.echo("This is a dry run. No changes will be made.")
        
        # Call the main organizing function
        organize_files(path, by, dry_run)

if __name__ == '__main__':
    cli()
