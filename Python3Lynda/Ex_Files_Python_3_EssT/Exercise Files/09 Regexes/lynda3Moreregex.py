#!/usr/bin/python3


import re

#def main():
    #fh = open('raven.txt')
    #for line in fh:
    #    print(re.sub('(Len|Neverm)ore', '###', line), end='') #sub actually means search and replacing with # marks

def main(): #this example is printing out just the lines we searched and replaced
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore',line)
        if match:
            print(line.replace(match.group(), '###'),end='')




if __name__ == "__main__": main()

