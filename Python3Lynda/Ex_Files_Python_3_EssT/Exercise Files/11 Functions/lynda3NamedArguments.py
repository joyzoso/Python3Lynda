#!/usr/bin/python3


def main():
    testfunc(4, 5, 6, 7, 8, 9, one = 1, two = 2, seven = 3)


#def testfunc(here, there, everywhere, *args, **kwargs): #Keyword args, kwargs is a dictionary
    #print('This is a test function',
    #  here, there, everywhere, args, #notice args is in a tuple
    #  kwargs['one'], kwargs['two'], kwargs['seven'])

def testfunc(here, there, everywhere, *args, **kwargs):
    #for k in kwargs: print(k, kwargs[k]) #this is commented to see the example below
    for n in args: print(n)


if __name__ == "__main__": main()

