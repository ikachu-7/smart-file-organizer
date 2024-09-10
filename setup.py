from setuptools import setup, find_packages

setup(
    name='file-organizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'organize = file_organizer.cli:cli',
        ],
    },
    author='Gojo Satoru',
    description='A CLI tool to organize files in directories by type or date.',
)
