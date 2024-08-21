import pytest

from isPrime import isPrime

def testIsPrime():
    assert isPrime(5) == True
    assert isPrime(11) == True

testIsPrime()