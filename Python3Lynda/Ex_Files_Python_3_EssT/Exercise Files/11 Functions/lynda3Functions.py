#!/usr/bin/python3

def main():
    testfunc(88, 7) #note here that '7' is used and not the default value below

def testfunc(number, another = 53, onemore = 80): #you can pass these, like above or give thm default values by assigning them here in the function definition
    pass #this is NOOP, stub/placeholder that you can use if you need to have something inside the body when creating functions
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main() #this allows you to call a function before it is defined
