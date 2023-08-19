# Name-Format-auto
Auto name format program with Python
Design for setting the name on excel files to be on the format of dd/mm/yyyy for all the files on the folder

This program gets inputs from the user as to which month and year it should use, and what folder the files to be renamed should be.
The program will then rename all the files with an extension of either .xls or .xlsx and only them, starting with 01/mm/yyyy to the last file on the folder

Inputs that are not on this format will not be accepted.

TODO: reject empty inputs, as the user shouldn't be able to run the program with any of the inputs empty,
      upgrade the interface
      get the whole program to run as an executable(.exe) file
      create a script where the program would detec if the worked month and year should have as many days as there are files on the folder
      i.e. having 31 files and the user input 02 as month. The program should warn the user that the number of files exceeds the number of days on that month, and then rename on the right amount of files. 
      make the program also modify a certain cell on the same input as the file.
      Create a prompt that'll ask the user if they want to rename more files when it's finished.
