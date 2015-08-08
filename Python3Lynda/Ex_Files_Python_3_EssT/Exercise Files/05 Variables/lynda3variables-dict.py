#!/usr/bin/python3

#def main():
   # d = { 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
   # for k in sorted(d.keys()): #sorting the keys in alpha order
       # print(k, d[k])

def main(): #another easier way to create a dict
    d = dict(
        one = 'Joy', two = 'wee', three = 3, four ='hi', five = 5
    )
    d['hello'] = 6
    for k in sorted(d.keys()): #sorting the keys in alpha order
        print(k, d[k])

if __name__ == "__main__": main()

