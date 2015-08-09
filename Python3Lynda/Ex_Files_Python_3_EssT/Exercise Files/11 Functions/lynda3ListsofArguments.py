#!/usr/bin/python3

def main():
    testfunc(10, 9, 8, 7, 6, 5, 4)

def testfunc(here, there, everywhere, *args):
    print(here, there, everywhere, args) #adding args here gives us a tuple
    for n in args: print(n, end=' ') # lists the arbitrary arguments after named arguments

if __name__ == "__main__": main()
