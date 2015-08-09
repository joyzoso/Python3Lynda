#!/usr/bin/python3


class Duck:
    #def __init__(self, color = 'brown'): #the below is a better way
        #self._color = color
    def __init__(self, **kwargs):
        #self._color = kwargs.get('color', 'brown') #setting default value to brown
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    #def set_color(self, color): #this method and the one allows more control and easier to track
       # self._color = color
        #self.variables['color'] = color

   # def get_color(self): #this and the above are called accessor methods and helps to avoid side effects
        #return self._color
       # return self.variables.get('color', None)

        ############the above two methods are commented out entirely to show that the below is even more efficient

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet = 2)
    donald.set_variable('color', 'black')
    #print(donald._color)
    # donald._color = 'blue'
    # print(donald._color)
    #print(donald.get_color())
    #donald.set_color('purple')
    #print(donald.get_color())
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))

if __name__ == "__main__": main()

