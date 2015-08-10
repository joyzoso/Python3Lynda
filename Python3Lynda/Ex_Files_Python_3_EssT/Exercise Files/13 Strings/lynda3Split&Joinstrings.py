#!/usr/bin/python3


def main():
    s = 'hey hey hey, this is a string'
    print(s)
    print(s.split()) #split method
    print(s.split('i'))
    words = s.split()
    print(words)
    for w in words: print(w)
    new = ':'.join(words) #join method
    print(new)
    print(', '.join(words))


if __name__ == "__main__": main()
