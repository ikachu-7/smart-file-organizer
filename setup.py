from setuptools import setup, find_packages

setup(
    name='SmartFileOrganizer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'organize = file_organizer.cli:cli',
        ],
    },
    author='Gojo',
    description='A CLI tool to organize files in directories by type or date.',
)
