# Code Breaker
# Reads in sample Encrypted file and and decrypts and prints messages in file
#
# Copyright 2014, Jason Kolankowski, Preyanshu Kumar.
# All rights reserved.
#
# Created:		Jason Kolankowski(<kolankow@ualberta.ca>)
#                       Preyanshu Kumar (<preyansh@ualberta.ca>)
# Imports
import sys

# Functions global dictionaries and lists

alpha = {1:'A',2:'B',3:'C',4:'D',5:'E',
         6:'F',7:'G',8:'H',9:'I',10:'J',
         11:'K',12:'L',13:'M',14:'N',15:'0',
         16:'P',17:'Q',18:'R',19:'S',20:'T',
         21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

#
#read in a file
def read_file():
    input_file=input('Enter the input filename: ')
    try:
        open_file=open(input_file,'r')
    except IOError:
        print('File does not exist!')
        sys.exit()
    
    #reads each line of the file    
    file=open_file.readlines()
    open_file.close()
    
    #Clean up the file
    codebrk_file=[]
    for code in file:
        codebrk=code.strip()
        codebrk_file.append(codebrk)
    #print(codebrk_file) # Test line
        
    #returns the file with each line as a list
    return codebrk_file

def decoded_file(file):
    # find what is to be decoded and the key
    for line in file:
        codeAnd_key= line.split()
        #print(codeAnd_key) #Test Line
        #check for both components, assume that the message is always there
        if len(codeAnd_key)<2:
            print('Missing Key!')
        else:
            message = list(codeAnd_key[0])
            key = int(codeAnd_key[1])
            #print(key) # Test line
            #print(message) # Test Line
            
            #decode each letter
            d_list=[]
            for letter in message:
                raw_value = ord(letter)
                i_value= (raw_value - 64)
                #print(i_value)   # Test Line
                value = i_value - key
                if value < 1:
                    value = value + 26
                #print(value) # Test Line
                d_letter = alpha[value]
                #print(d_letter) # Test Line
                d_list.append(d_letter)
            
            # output the decoded message
            d_message = ''.join(d_list)
            print(d_message)

def main():
    evlfile = read_file()
    #print(evlfile) #Test Line
    decoded_file(evlfile)

main()
