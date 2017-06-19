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
from collections import deque

class Tree:
    def __init__(self, cargo ,left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def make_tree():
    
    t = Tree("S", Tree("A", Tree("B", Tree("C"), Tree("E", Tree("D"), Tree("F", Tree("G")))),
    Tree("D", Tree("E", Tree("B", Tree("C")), Tree("F", Tree("G"))))), Tree("D", Tree("A", Tree("B", Tree("C"),
    Tree("E", Tree("F", Tree("G"))))), Tree("E", Tree("B", Tree("A"), Tree("C")), Tree("F", Tree("G")))))
    return t


def sort():
    print("lol")

def hill_climb(q):
    print ("Hill climb")

    t = make_tree    

    
    
    #While there are elements in the queue
        #print ()
        

def main():

    q = queue.LifoQueue()
    #q.put("S") # Create first root object

    #q = deque("S")
    #q.appendleft('A')

    
    
    print("Hello World")
    hill_climb(q)
    #Hill_climb
    
    
    

main()