# file_functions.py
# Modules for working with files
#
# Usage: python3 merge_main.py filename
# Created - Mark O.P

from pathlib import Path
import os
def write_sorted_list_to_file(filename, sorted_list):
    """ Takes a sorted list, and writes it out to desired filename

    Parameters
    ----------
    filename: string
        Name of file you want your sorted list written out to

    data_list: list
        Sorted list, take ints and write out to file_name
    """
    
    outfile = open (filename, 'w')
    
    for value in sorted_list :
        aline = str(value) + "\n"
        outfile.write(aline)
    
    outfile.close()

# Tutorial on files, used 2 lines of code and expanded
# https://realpython.com/working-with-files-in-python/
def get_folder_files(folder_name):
    """ Takes a folder name and pulls all .txt files into list

    Parameters
    ----------
    folder_name: string
        Name of folder we are pulling .txt files from

    Returns
    -------
    list
        List of all the .txt files to run tests on for merge_sort
    """

    cwd = os.getcwd()
    folder_list = []
    folder_path = cwd + "/" + folder_name
    folder_path_object = Path(folder_path)
    files_in_path = folder_path_object.iterdir()
    for files in files_in_path:
        file_string = str(files)
        # UnicodeDecodeError: 
        # 'utf-8' codec can't decode byte 0x80 in position 3131:
        # .DS_Store was problem, could not see with BBEdit
        if (file_string.find(".DS_Store") < 0):
            # Don't want to test files that have been sorted
            if(file_string.find("sorted") < 0):
                folder_list.append(file_string)
    
    return folder_list


