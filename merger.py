from PyPDF2 import PdfFileMerger
import os.path
import datetime


def get_number_of_files():
    number_of_files = 0

    while number_of_files < 2:

        input_value = input('How many files would you like to merge? ')
        number_of_files = int(input_value)
        if int(number_of_files) < 2:
            print("You need at leat two files to proceed")

    return number_of_files


def get_file_paths(number_of_files):

    file_paths = []

    for i in range(number_of_files):

        while True:
            file_path = input('Enter path of file #' + str(i + 1) + ': ')

            if os.path.exists(file_path):
                if file_path[4:] == '.pdf':
                    file_paths.append(file_path)
                    break
                else:
                    print('File must be of type PDF')
            else:
                print('Invalid file path! ')
    return file_paths


def get_destination_target():

    while True:
        destination_target = input('Enter path to store result: ')

        if os.path.exists(destination_target):
            return destination_target
        else:
            print('Invalid file path! ')


def merge(path_to_files, result_path):
    merger = PdfFileMerger()

    for pdf in path_to_files:
        merger.append(open(pdf, 'rb'))

    date = str(datetime.datetime.now())[:10].replace('-', '_')
    file_path = result_path + '/result_' + date + '.pdf'

    with open(file_path, 'wb') as result:
        merger.write(result)

    if os.path.exists(file_path):
        return True
    else:
        return False


print(' _______________________________________')
print('|    ____  ____  _____                  |')
print('|   |  _ \|  _ \|  ___|                 |')
print('|   | |_) | | | | |_                    |')
print('|   |  __/| |_| |  _|                   |')
print('|   |_|  _|____/|_|                     |')
print('|   |  \/  | ___ _ __ __ _  ___ _ __    |')
print('|   | |\/| |/ _ \ `__/ _` |/ _ \ `__|   |')
print('|   | |  | |  __/ | | (_| |  __/ |      |')
print('|   |_|  |_|\___|_|  \__, |\___|_|      |')
print('|                    |___/              |')
print('|_______________________________________|')
print('')
print('Welcome to PDFMerger!')
print('')

number_of_files = get_number_of_files()
files_to_merge = get_file_paths(number_of_files)
destination_target = get_destination_target()


if merge(files_to_merge, destination_target):
    print('Files have now been merged successfully!')
else:
    print('Unknown error..')
