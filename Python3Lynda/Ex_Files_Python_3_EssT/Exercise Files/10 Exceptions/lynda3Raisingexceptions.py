#!/usr/bin/python3


def main():
    try:
        for line in readfile('lines.doc'): print(line.strip()) #add an x or what have you to throw the error
    except IOError as e:
        print('no can read file, yo!', e)
    except ValueError as e:
        print('bad filename', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('filename must end with .txt')

if __name__ == "__main__": main()

