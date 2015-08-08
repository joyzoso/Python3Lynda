a,b = 0,1
x,y = 'zero', 'one'
if a < b and x < y: print('yes')
else: print('no')

list=[1,2,3,4,5,6,7,8,9,10]

print(list[0:5]) #this is called a slice

print(range(0,10)) #this is an iterable
for i in range(0,10): print(i)

list[:] = range(100) #note that range actually includes 0 to 99
print(list)
print(list[27]) #giving a slice that begins at index 27
print(list[25:35]) #note does not give you '35'
print(list[25:35:4]) #gives you every 4th element
for i in list[25:35:4] : print(i)
list[25:35:4]=(99,99,99) #note replacing with '99'
print(list)

#slice operators have 3 arguments: the start, the stop and the step, yo!