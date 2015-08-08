#!/usr/bin/python3

import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE) #could just use the 'I' but better to use ingnorecase
    for line in fh:
        if re.search(pattern,line):
            print(pattern.sub('###',line), end='')

if __name__ == "__main__": main()

