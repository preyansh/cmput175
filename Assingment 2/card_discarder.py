#read in a file
import sys

#variables and global list
k=0
n=0
dis_List=[]

class Stack:
    
    def __init__(self):
        self.stack = [] # start with an empty stack
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
class Deck(file):
    
    def __init__(self):
        self.deck = deckf----------------

    def __str__(self):
        return ('The last'+len(k)+'cards discarded are: '+discarded_list+'/n'+'The remaining cards are'+remainder_list)
    
class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.queue)


    
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
    
   
        
    #returns the file as a list of numbers from 1 to length of code[0]
    return n

def main():
    file=read_file()
    d=Deck(file)