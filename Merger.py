
from PyPDF2 import PdfFileMerger
import os.path
import datetime


def merge(path_to_files, result_path):

	merger = PdfFileMerger()

	for pdf in path_to_files:
		merger.append(open(pdf, 'rb'))

	date = str(datetime.datetime.now())[:10].replace('-','_')
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

file_paths = []

number_of_files = input('How many files would you like to merge? ')




for i in range(int(number_of_files)):

	file_path = input('Enter path of file #' + str(i) + ': ')
	if os.path.exists(file_path):
		file_paths.append(file_path)
	else: 
		print('Invalid file path! ')



result_path = input('Enter path to store result: ')

if merge(file_paths, result_path):
	print('Files have now been merged succsessfully!')
else: 
	print('Something went wrong!')




#	/Users/olavfykse/Desktop/PDFMerger/file1.pdf 
#	/Users/olavfykse/Desktop/PDFMerger/file2.pdf 
#	/Users/olavfykse/Desktop 
