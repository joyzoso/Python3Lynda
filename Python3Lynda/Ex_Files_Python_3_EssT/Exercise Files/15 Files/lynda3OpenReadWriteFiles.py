#!/usr/bin/python3


#def main():
#    f = open('lines.txt', 'r') #open function
#    for line in f.readlines():
#         print(line, end = '')




def main():
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('done')

    #the above is a simple way to write to a text file

if __name__ == "__main__": main()
