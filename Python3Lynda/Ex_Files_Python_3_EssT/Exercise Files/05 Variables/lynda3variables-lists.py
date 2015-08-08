#!/usr/bin/python3


#def main():
   # x = (1,2,3) #tuple, this is a mutable object-once created, cannot change
   # print(type(x), x)
   # x = [1,2,3] #this is a list type and it IS mutable, can be changed/modified
   # x.append(5)
   # x.insert(0,7) #adding the 7 at the zero index
   # print(type(x), x)

#def main():
   # x = "excellent"
   # print(type(x), x[4:8]) #this is a slice

def main():
    x = ('a', 'b','c','d','e')
    y = 'excellent'
    for i in x,y:
        print(i)

if __name__ == "__main__": main()


