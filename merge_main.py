# merge_main.py
# Main program to run merge sort on list of files
#
# Usage: python3 merge_main.py filename
# Created - Mark O.P
import merge_sort as ms
import file_functions as f
import sys
import os

def read_integers(filename):
    """ Takes a file(list of ints) and reads them into a python list

    Parameters
    ----------
    filename: string
        File to pull ints from into a python list

    Returns
    -------
    list
        returns list of ints from file passed
    """
    
    integer_list = []
    #print(file_name)
    
    infile = open(filename, 'r')
    flag = True

    while (flag):
        temp = infile.readline()
        try:
            temp = int(temp)
            integer_list.append(temp)
        except ValueError:
            flag = False

    #always close files after done using them
    infile.close()
            
    return integer_list

def make_copies_list(list_to_copy):
    """ Takes a list, and makes a quarter and a half copy of it

    Parameters
    ----------
    list_to_copy: list
        List to pull ints from into our new lists quarter/half list
    
    Returns
    -------
    lists
        returns two lists, a quarter and a half copy starting
        from the beginning of the original list
    """

    num_quarter = len(list_to_copy) // 4
    quarter_list = []
    num_half = len(list_to_copy) // 2
    half_list = []

    for i in range (0, num_quarter):
        quarter_list.append(list_to_copy[i])
    
    for j in range (0, num_half):
        half_list.append(list_to_copy[j])
    
    return quarter_list, half_list


def main():
    """ Creates list from numgen.py, puts ints into list, and sorts them.

    Takes a command line argument for filename of random list of ints
    then calls read_integers to put those ints into a list. List will
    be printed as is, and then print the sorted list after calling 
    merge_sort. Number of comparisons/assignments that merge_sort
    did will also be printed to the terminal.
    """

    cwd = os.getcwd()
    infile = sys.argv[1]

    if(infile.find('.txt') > 0):
        files_to_test = [infile]
    else:
        files_to_test = f.get_folder_files(infile)
        cwd = cwd + "/" + infile


    for file in files_to_test:

        random_list = read_integers(file)
        random_quarter_list, random_half_list = make_copies_list(random_list)
        list_sizes = [random_quarter_list, random_half_list, random_list]
        num_ints = ["quarter", "half", "full"]
        counter = 0

        for lists in list_sizes:
            print("Random list of", len(lists), "integers")
            print("--------------------------------------")
            #print (lists)
            comparisons, assignments = ms.merge_sort(lists, 0, len(lists) - 1)
            print("\nSorted list:")
            #print(lists)
            print()
            print("Number of ints sorted:", len(lists))
            print("Number of comparisons:", comparisons)
            print("Number of assignments:", assignments)
            # insert sorted to filename, assign to outfile != overwrite
            index = file.find(".txt")
            outfile = file[:index] + "-sorted" + num_ints[counter] + file[index:]
            f.write_sorted_list_to_file( outfile, lists)

            print("Sorted list put in: " + cwd)
            counter += 1
            print() 
            print()


if __name__ == "__main__":
    main()
