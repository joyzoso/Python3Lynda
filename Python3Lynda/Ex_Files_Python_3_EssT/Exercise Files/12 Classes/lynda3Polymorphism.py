#!/usr/bin/python3


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def roar(self):
        print('The Duck can\'t roar')

    def fur(self):
        print('Ducks have feathers')

class Bear:
    def roar(self):
        print('rawr')

    def fur(self):
        print('The bear has brown fur')

    def walk(self):
        print('Meanders like a bear')

    def quack(self):
        print('Bears do not quack!')


def main():
    donald = Duck()
    grizzly = Bear()
    in_the_forest(donald)
    in_the_pond(grizzly)

def in_the_forest(Bear):
    Bear.roar()
    Bear.fur()

def in_the_pond(Duck):
    Duck.quack()
    Duck.walk()



if __name__ == "__main__": main()

