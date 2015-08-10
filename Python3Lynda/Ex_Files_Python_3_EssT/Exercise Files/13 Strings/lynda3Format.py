x, y = 8, 99
print(x,y)
print('this is {}, that is {}'.format(x,y))

#allows you to put placeholders in a string and then replace those placeholders
# with values and return a new string

print('this is {} and that is {}'.format(x,y))
print('this is {1}, that is {0}, this too is {1}'.format(x,y))
d = dict(tom = x, jerry = y)
print('this is {tom} and that is {jerry}'.format(**d))

z = 'this is {}, that is {}'
print(z)
print(z.format(x,y))
print(id(z))

