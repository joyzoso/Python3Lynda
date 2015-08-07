
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e: #this allows the actual error to be displayed
    print("something bad happened ({})".format(e))

print("after badness")

