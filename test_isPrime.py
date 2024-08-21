import pytest

from isPrime import isPrime

def testIsPrime():
    assert isPrime(5) == True
    assert isPrime(7) == True

testIsPrime()