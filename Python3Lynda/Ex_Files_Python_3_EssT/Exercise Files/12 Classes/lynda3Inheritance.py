#!/usr/bin/python3

class Animal:
    def talk(self): print('This is what I sound like!')
    def walk(self): print('This is how I walk')
    def clothes(self): print('This is what I wear')


class Duck(Animal): #Duck can inherit all the above methods from Animal, basically we now say Duck is an animal
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk() #this built in function accesses the parent class
        print('Walks like a duck.')

class Bear(Animal):
    #pass  #remember this is a place holder if needed
    def clothes(self):
        print('I have brown fur, rawr!')

def main():
    donald = Duck()
    donald.quack()
    donald.walk() #note that 'walk' in Duck overrides 'walk' in Animal
    donald.clothes()

    grizzly = Bear()
    grizzly.walk()
    grizzly.clothes()

if __name__ == "__main__": main()
