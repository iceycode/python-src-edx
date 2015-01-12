'''
Dynamic Programming example
Memoization

'''


# Standard fibonacci solution
# doubly recursive, but extra work
def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def testFib(n):
    assert type(n) == int and n >=  0
    for i in range(n):
        print ('fib of', i, '=', fib(i))

testFib(5)


def fastFib(x, memo):
    # checks to see if x is in dictionary
    assert type(x) == int and x >= 0 and type(memo) == dict

    #base case: compute
    if x == 0 or x == 1:
        return 1

    # if x is in memo;
    if x in memo:
        return memo[x]
    result = fastFib(x-1, memo) + fastFib(x-2, memo)
    memo[x] = result
    return result

def testFastFib(n):
    assert type(n) == int and n >=  0
    for i in range(n):
        print ('fib of', i, '=', fastFib(i, {}))

#testFib(32); #slows down; since redunant computations
testFastFib(32) #WAY faster; almost linear; virtually no slow down