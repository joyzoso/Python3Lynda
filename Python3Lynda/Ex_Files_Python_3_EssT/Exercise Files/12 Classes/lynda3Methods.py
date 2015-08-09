#!/usr/bin/python3

class Duck:
    def __init__(self, value): #init is a special method used as a constructor initializes data
        #print('constructor')
        self._v = value #this value is actually attached to the object and not the class aka encapsulation

    def quack(self): #the first argument to these functions (methods) is the self, which refers to the object.
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(88)
    tom = Duck(77)
    donald.quack() #the dot operator is used to reference an attribute (method) on the object (ie: donald)
    donald.walk() #the donald object gets passed to the walk method
    tom.quack()
    tom.walk()

if __name__ == "__main__": main()

