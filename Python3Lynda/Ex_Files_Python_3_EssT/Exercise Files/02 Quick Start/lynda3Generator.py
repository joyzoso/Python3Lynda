

def isprime(n): #utility function
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1): #this is the generator
   while(True):
       if isprime(n): yield n
       n += 1 

for n in primes(): #uses the generator function above as an iterator
    if n > 100: break
    print(n)

