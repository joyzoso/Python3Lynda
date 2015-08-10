#!/usr/bin/python3

d = {'one':1, 'two':2, 'three':3}
print(d)

d = dict(one=1, two=2, three=3)
print(d)
print(type(d))
x = dict( four = 4, five = 5, six = 6 ) #this is an easier way to type a dict
print(x)
d = dict(one = 1, two = 2, three = 3, **x)
print(d)
print('four' in x)
print('three' in x)
for k in d: print(k) #for key in d, print key
for k, v in d.items(): print(k,v) # for key, values in d....
print(d['three'])
print(x.get('three')) #note that it returns the none value
print(d.get('three'))
print(x.get('three', 'not found')) # as opposed to returning a none value
del x['four']
print(x)
print(x.pop('five'))
print(x)
