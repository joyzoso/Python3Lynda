#!/usr/bin/python3

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('needs at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):
        i = self.start #sets the starting point
        while i <= self.stop:
            yield i # this allows for execution to be picked up after this statement the next time a func is called
            i += self.step

def main():
    o = inclusive_range(1, 25, 3, 7) #try with no arguments, 1, 4, etc to raise errors and test out this iterable for loop
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()