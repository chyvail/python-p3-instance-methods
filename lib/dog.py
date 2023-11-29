#!/usr/bin/env python3
import ipdb

class Dog:
    # Class body goes here

    #Instance method definition what this dog can do
    def bark(self): # needed with instance methods ; // method --> function within a class
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
