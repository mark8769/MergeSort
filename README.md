## **Purpose**

Implementation of the Merge Sort algorithm in python. Testing merge sort to show that it runs in NlogN time.
Finished project has the functionality of passing in a folder name of .txt files to run tests on.

## **Contents**

For this project we will have 4 files:

1. merge_main.py - Entry point of the project.
2. merge_sort.py - Merge sort implementation
3. numgen.py - Writes random numbers to a file given some range, and filename.
4. file_functions.py - Functions to read and write to files.

## **How to use**

There are two ways to run this program:

1. Pass in a file name in .txt format
2. Pass in a folder name from your current working directory, with .txt files

- if following 2nd way, you can repeat 1st step for desired amount of files, and put in folder.

## **1st Step**

-Creating a random list of integers in .txt format.

-issue this command:

```
python3 numgen.py filename quantity range_size
```

filename: Name of file. Either .txt format, or folder name.

quantity: amount of integers you would like to make

range_size: range of integers -size / 2 to  +size / 2

## **2nd Step**

-All we need for this is the filename from last command or a folder name

-issue this command:

```
python3 merge_main.py filename.txt
```

-or

```
python3 merge_main.py foldername
```

### **NOTE**

- If Working with a folder you will have to create your own .txt files and put them inside a folder.

