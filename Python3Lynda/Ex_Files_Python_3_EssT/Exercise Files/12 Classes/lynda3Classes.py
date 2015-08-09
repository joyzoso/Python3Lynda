#!/usr/bin/python3

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck() #Donald is an object (an instance of Duck) of the class, Duck
    print(donald) #note the output lists .Duck object
    donald.quack() #the empty () means it will call the initial (self), therefore, quack
    donald.walk() #and this would print, 'walks like a duck'

#you call the methods of the Duck by using the .notation

if __name__ == "__main__": main()

