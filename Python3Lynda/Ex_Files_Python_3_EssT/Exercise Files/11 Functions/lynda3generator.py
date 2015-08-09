#!/usr/bin/python3


#def main():
    #print("This is the functions.py file.")
    #for i in inclusive_range(0, 35, 2): #range can be calld with 1,2, or 3 arguments
    #    print(i, end = ' ')


#def inclusive_range(start, stop, step):
   # i = start
   # while i <= stop:
   #     yield i #returns i, but the next time the function is called it will start again after yield.
   #     i += step

#the above two defining functions are meant to execute together, below is a separate example.


def main():
    print("This is the functions.py file.")
    #for i in inclusive_range(6, 35, 2, 8): #triggering adding an extra argument
    for i in inclusive_range(): #triggering by having no arguments
        print(i, end = ' ')


def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('needs at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, only have {}'.format(numargs))
    i = start
    while i <= stop:
        yield i #returns i, but the next time the function is called, execution picks up right after the yield
        i += step

if __name__ == "__main__": main()