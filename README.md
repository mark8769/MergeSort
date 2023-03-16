## **Purpose**

The purpose of project 1 is to implement the Merge Sort algorithm in python.
Alongside this we will be using git to make all our commits and tags when we have completed milestones.
We will also be learning more about commenting style guidelines for specific languages. At the end 
of this project we will be turning in a report with our results to show that Merge Sort runs 
in NlogN time. Our finished program will have the functionality of passing 
in a folder name of .txt files to run tests on.

## **Contents**

For this project we will have 8 files:

1. merge_main.py
2. merge_sort.py
3. numgen.py
4. file_functions.py
5. README.md
6. .gitignore
7. MergeSortReport.pdf
8. Report.docx (source for pdf document)

## **How to use**

There are two ways to run this program:

1. Pass in a file name in .txt format
2. Pass in a folder name from your current working directory, with .txt files

- if following 2nd way, you can repeat 1st step for desired amount of files, and put in folder.

### **1st Step**

-Creating a random list of integers in .txt format.

-issue this command:

**python3 numgen.py filename quantity range_size**

filename: Name of file. Either .txt format, or folder name.

quantity: amount of integers you would like to make

range_size: range of integers -size / 2 to  +size / 2

### **2nd Step**

-All we need for this is the filename from last command or a folder name

-issue this command:

**python3 merge_main.py filename.txt**

-or

**python3 merge_main.py foldername**

### **NOTE**

- If Working with a folder you will have to create your own .txt files and put them inside a folder.

