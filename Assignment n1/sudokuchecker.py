# Sudoko Checker
# Reads in sample Sudoku file and checks to see is file is a potential solution
#
# Copyright 2013, Jason Kolankowski, Preyanshu Kumar.
# All rights reserved.
#
# Created:		Jason Kolankowski(<kolankow@ualberta.ca>)
#                       Preyanshu Kumar (<preyansh@ualberta.ca>)
# Imports
import sys

# Functions constants and global lists
columns_list=[]

#read in a file
def read_file():
    input_file=input('Enter the input filename: ')
    try:
        open_file=open(input_file,'r')
    except IOError:
        print('File does not exist!')
        sys.exit()
    
    #reads each line of the file    
    sudoku_file=open_file.readlines()
    open_file.close()
    
    #returns the file with each line as a list
    return sudoku_file

#removes anything from the list that we do not want (/n, white spaces, etc.)
def clean_file(file):
    clean_list=[]#new empty list where our clean elements will go
    
    for row in file:
        clean_row=row.strip()#strips the element to just numbers
        clean_list.append(clean_row)
    return clean_list

#checks the rows of the file for duplicates
def analyze_row(rows):
    for row in rows:
        #new empty list where all numbers will go except for zero
        check_list=[]
        new_row_list=list(row)
        if len(new_row_list)>9:
            return False 
        
        #iterates over the individual numbers in our list
        for number in new_row_list:
            number=int(number)
            if number in check_list:
                return False
            
            #if number bigger than 0, then we append it
            if number > 0:
                check_list.append(number)
                #print(check_list) #test line
                
    return True 

# Uses a clean set of rows to create and analyze columns
def analyze_columns(rows):
    cl=[]
    c0=[]
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    c6=[]
    c7=[]
    c8=[]
    cl=[c0,c1,c2,c3,c4,c5,c6,c7,c8]
    for row in rows:
        row=list(row)
        i=0
        for d in row:
            l=cl[i]
            l.append(d)
            i += 1
    #print (cl)
    for column in cl:
        #column_string=''.join(column)
        #print (column_string)
        columns_list.append(column)
        #print(column_list)
        new_column_list=[]

        for digit in column:
            digit=int(digit)
            if digit > 0:
                if digit not in new_column_list:
                    new_column_list.append(digit)
                else:
                    return False
    return True

#Make and check 9 boxes from the columns data
def analyze_boxes(columns):
    master_list=[[0,1,2],[3,4,5],[6,7,8]]
    
    # get the columns in groups of 3
    for columns in master_list:
        c1= columns_list[columns[0]]
        c2= columns_list[columns[1]]
        c3= columns_list[columns[2]]
        
        #look at the rows of the columns in groups of 3
        for row_set in master_list:
            check_list=[]
            
            #make three rows and add them to the check list
            for row in row_set:
                r1= int(c1[row])
                r2= int(c2[row])
                r3= int(c3[row])
                #print(c1,c2,c3) #Test line
                
                # Check the 3x3 block
                if r1>0:
                    if r1 not in check_list:
                        check_list.append(r1)
                    else:
                        return False
                if r2>0:
                    if r2 not in check_list:
                        check_list.append(r2)
                    else:
                        return False                
                if r3>0:
                    if r3 not in check_list:
                        check_list.append(r3)
                    else:
                        return False       
            #print(check_list) #test line
    return True
            
            
def main():
    file=read_file()
    #print(file) #Test line
    
    rows_list=clean_file(file)
    #print(rows_list) #Test line
    
    rows_check=analyze_row(rows_list)
    #print(rows_check #Test line
    
    columns_check=analyze_columns(rows_list)
    #print(columns_check) #Test line
    
    box_check=analyze_boxes(columns_list)
    #print(box_check) #Test line
    
    #Check to see if all tests have pass and output result
    if box_check and columns_check and rows_check:
        print('The puzzle is valid!')
    else:
        print('The puzzle is not valid!')
    
    
main()
