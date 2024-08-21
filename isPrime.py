import math
def isPrime(x=1):
    if (x%2==0):
        return False
    for i in range(3, int(math.sqrt(x)), 2):
        if(x%i==0): 
            return False
    return True

print(isPrime(9)) 