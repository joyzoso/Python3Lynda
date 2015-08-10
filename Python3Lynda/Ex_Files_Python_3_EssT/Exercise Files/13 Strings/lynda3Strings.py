#!/usr/bin/python3


def main():
    'this is a string'.upper() #the string itself is an object
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha()) #checks for alpha characters
    print(s.isdigit()) #checks for digits
    print(s.isprintable()) #checks if all the characters in the strings ar printable
    '   this is a string  '.strip()
    s1 = "hey hey hey\n"
    print(s1.strip())


if __name__ == "__main__": main()

