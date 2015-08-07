


# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():  #.readlines is the actual iterator
    print(line)


fh = open('lines.txt')
for line in fh.readlines():
    print(line, end="") #this cleared the extra line
