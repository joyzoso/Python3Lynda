#!/usr/bin/python3

import re

def main():
    fh = open('raven.txt')
    for line in fh: #reading the file, line by line
        match = re.search('(Len|Neverm)ore', line)
        if match:
       # if re.search('(Len|Neverm)ore', line): #matches lenore or nevermore
       #     print(line, end='') #avoid putting blank lines in between
            print(match.group()) #this prints all the words that we actually matched (2 lines above commented out)

if __name__ == "__main__": main()

