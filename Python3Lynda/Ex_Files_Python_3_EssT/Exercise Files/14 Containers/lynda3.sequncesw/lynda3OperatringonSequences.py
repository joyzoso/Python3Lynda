
t = tuple(range(30))
print(t)
print(type(t))
print(10 in t)
print(50 in t)
print(50 not in t)
print(t[10])
print(len(t))
for i in t: print(i) #iterate it!
x = list(range(20))
print(x)
print(10 in x)
print(20 in x)
for i in x: print(i)
#you can do any operation on a tuple that does not involve modifying it
print(t.count(5)) #how many 5's are in the tuple
print(t.index(5))
print(x.append(100))
print(x)
print(len(x))
print(x.extend(range(20)))
print(x)
print(x.insert(0,25))
print(x)
print(x.insert(15,88))
print(x)
del x[12] #deletes the 12th element
print(x)
x.pop() #takes off the last element
print(x)
x.pop(0) #pops from the beginning of the list
print(x)

