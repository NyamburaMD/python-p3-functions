#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")

def greet(name):
    print (f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print (f"Hello, {name}!")

def add(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)) :
        return None
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2


