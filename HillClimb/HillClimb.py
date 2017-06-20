#!/usr/bin/python
# CSC 547 Artificial Intelligence
# Lecturer: Sung Shin
# 
# Date: 6/17/2017
# Author: Markus Haugsdal
#
# Resources used: https://www.tutorialspoint.com/python/index.htm
#                 http://openbookproject.net/thinkcs/python/english3e/trees.html
#
# Homework 2 
# Due date: 6-21
#
#
# This is an implementation of the Beam Search Algorithm, using the test data from figure 4.2 in the class notes.


import queue
import copy
from collections import deque

class Tree:
    def __init__(self, cargo, level = None ,left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def make_tree():
    
    t = Tree("S", 0 , Tree("A", 1, Tree("B",2, Tree("C", 3), Tree("E", 3, Tree("D", 4), Tree("F", 4, Tree("G",5)))),
    Tree("D", 2, Tree("E",3, Tree("B",4, Tree("C",5)), Tree("F",4, Tree("G",5))))), Tree("D",1, Tree("A",2, Tree("B",3, Tree("C",4),
    Tree("E",4, Tree("F",5, Tree("G",6))))), Tree("E",2, Tree("B",3, Tree("A",4), Tree("C",4)), Tree("F",3, Tree("G",4)))))

#    t = Tree("S", 0 , Tree("A", 1, Tree("B",2, Tree("C", 3), Tree("E", 3, Tree("D"), Tree("F", Tree("G")))),
 #   Tree("D", Tree("E", Tree("B", Tree("C")), Tree("F", Tree("G"))))), Tree("D",1, Tree("A", Tree("B", Tree("C"),
  #  Tree("E", Tree("F", Tree("G"))))), Tree("E", Tree("B", Tree("A"), Tree("C")), Tree("F", Tree("G")))))


    return t


def sort(q):
    
    
    q2 = queue.PriorityQueue
    q2.queue = copy.deepcopy(q.queue)

    i = q.qsize()
    
    while i > 0:
        temp = q.get()
        
        print("Cargo",temp.cargo)
        #q2.put(temp.cargo, temp)
        i-=1

    q.queue = copy.deepcopy(q2.queue)
    


def hill_climb(q):
    print ("Hill climb")

    t = make_tree()    
    
    goalNode = "G"

    #Enter root into a queue
    q.put(t)
 
    #While there are elements in the queue
    while q.qsize() != 0:
        print ("Hill climb")
        t = q.get()
               

        #Determine if first element is goal node
   
        print("Current node:",t.cargo)

        
        #2a if the first element is the goal node, break
        if t.cargo == goalNode:
            print("Goal found! Success!")
            break;
    
        #2b else, 
        else:
            #Remove first element from the queue(Done at the beginning) and sort the first elements children. Enter at the FRONT of the queue.
            
            if t.left != None:
                q.put(t.left)
            if t.right != None:
                q.put(t.right)

            #Sort!
            sort(q)
            

def main():

    q = queue.LifoQueue()
    hill_climb(q)

main()