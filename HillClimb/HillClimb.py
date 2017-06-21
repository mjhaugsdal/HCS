#!/usr/bin/python
# CSC 547 Artificial Intelligence
# Lecturer: Sung Shin
# 
# Date: 6/21/2017
# Author: Markus Haugsdal
#
# Resources used: https://www.tutorialspoint.com/python/index.htm
#                 http://openbookproject.net/thinkcs/python/english3e/trees.html
#
# Homework 2 
# Due date: 6-21
#
#
# This is an implementation of the Hill Climbing Algorithm, using the test data from figure 4.2 in the class notes.


import queue
import copy
from collections import deque

# Tree class. 

class Tree:
    def __init__(self, cargo, weight = None ,left=None, right=None):
        self.weight = weight
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

# Function to create tree from Fig 4.2 / 4.1
# (Messy)

def make_tree():
    
    t = Tree("S", 0 , Tree("A", 3, Tree("B",4, Tree("C", 4), Tree("E", 5, Tree("D", 2), Tree("F", 4, Tree("G",3)))),
    Tree("D", 5, Tree("E",2, Tree("B",5, Tree("C",4)), Tree("F",4, Tree("G",3))))), Tree("D",4, Tree("A",5, Tree("B",4, Tree("C",4),
    Tree("E",5, Tree("F",4, Tree("G",3))))), Tree("E",2, Tree("B",5, Tree("A",4), Tree("C",4)), Tree("F",4, Tree("G",3)))))

    return t

# Simplified print tree function

def print_tree(q):
    
    print("The following nodes were selected")
    while q.qsize() !=0 :
        t = q.get()
        #print(q.qsize())
        print(t.cargo)
    
# Sort function
# Input: Queue
# Output: Sorted Queue

def sort(q):
    
    
    q2 = queue.Queue()

    i = q.qsize()
    l = list(q.queue)

    while i > 0:
        temp = q.get()

        l.sort(key=lambda x:x.weight, reverse = True)
        q2.put(l[i-1])

        i-=1

    #q.queue = copy.deepcopy(q2.queue)
    return q2

# Hill climbing algorithm.
# Input: Queue with root node of tree
# Output: Void

def hill_climb(q):
    #print ("Hill climb")

    t = make_tree()    
    
    goalQueue = queue.Queue()
    goalNode = "G"

    #Enter root into a queue
    q.put(t)
 
    #While there are elements in the queue
    while q.qsize() != 0:
   
        t = q.get()
        goalQueue.put(t)
        
        #Determine if first element is goal node
        
        #2a if the first element is the goal node, break
        if t.cargo == goalNode:
            print("Goal found! Success!")
                      
            print_tree(goalQueue)
            
            break;
    
        #2b else, 
        else:
            #Remove first element from the queue(Done at the beginning) and sort the first elements children. Enter at the FRONT of the queue.
            
            if t.left != None:
                q.put(t.left)
            if t.right != None:
                q.put(t.right)

            #Sort!
            q = sort(q)
            
def main():

    q = queue.LifoQueue()
    hill_climb(q)

main()