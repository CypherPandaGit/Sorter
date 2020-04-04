import os
import sys
from pathlib import Path


# This will be new directories HTML, IMAGES, AUDIO etc.
dirs = {
    'Web': ['.html', '.htm'],
    'Zips': ['.exe', '.zip', '.rar'],
    'Documents': ['.docx', '.doc', '.pdf', '.xls', '.odt'],
    'Images': ['.jpg', '.jpeg', '.gif', '.bmp', '.png', '.psd', '.heif'],
    'Videos': ['.mp4', '.avi', '.flv', '.mov', '.mpeg'],
    'Audio': ['.mp3', '.aac', '.wav']}

# Only verification if directories in dictionary are created
# for value in dirs.items():
#     print(value)

# Remapping dirs to file_formats; for example: '.doc': 'DOCUMENTS'
file_formats = {file_extension: directory
                for directory, file_formats in dirs.items()
                for file_extension in file_formats}

# Just check if everything is OK
# for value in file_formats.items():
#     print(value)
#
# print(os.listdir('.\\'))


def organize_files():
# Main sorting function. It will check if directory exists. If yes; continune.
# If not; new directory will be created


    print('Do you want to organize your files automatically?\nYes  or  No')
    answer = input()

    if answer.lower() == 'yes' or answer.lower() == 'y':

        for entry in os.scandir():
            if entry.is_dir():
                continue

            file_path = Path(entry)
            file_extension = file_path.suffix.lower()

            if file_extension in file_formats:
                directory_path = Path(file_formats[file_extension])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))

            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass

        print('---------------')
        print('-----DONE!-----')
        print('---------------')
        print('THAT WAS SIMPLE')
        print('---------------')

    elif answer.lower() == 'no' or answer.lower() == 'n':
        print('----------------')
        print('You answered No.')
        print('----------------')
        sys.exit()

    else:
        print('--------------------')
        print('Something went wrong')
        print('--------------------')


if __name__ == '__main__':
    organize_files()
