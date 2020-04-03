import os
from pathlib import Path


# This will be new directories HTML, IMAGES, AUDIO etc.
dirs = {
    'HTML': ['.html', '.htm'],
    'EXE': ['.exe', '.zip', '.rar'],
    'DOCUMENTS': ['.docx', '.doc', '.pdf', '.xls', '.odt'],
    'IMAGES': ['.jpg', '.jpeg', '.gif', '.bmp', '.png', '.psd', '.heif'],
    'VIDEOS': ['.mp4', '.avi', '.flv', '.mov', '.mpeg'],
    'AUDIO': ['.mp3']}

# Only verification if directories in dictionary are created
for value in dirs.items():
    print(value)

# Remapping dirs to file_formats; for example: '.doc': 'DOCUMENTS'
file_formats = {file_extension: directory
                for directory, file_formats in dirs.items()
                for file_extension in file_formats}

# Just check if everything is OK
for value in file_formats.items():
    print(value)
