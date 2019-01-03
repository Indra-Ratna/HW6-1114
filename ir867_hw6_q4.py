#Indra Ratna
#CS-UY 1114
#27 Oct 2018
#Homework 6
#Problem 4

def double(n):
    # signature: int -> int
    # return doubled value of parameter
    return n * 2
def succ(n):
    # signature: int -> int
    # returns successor of parameter
    return n + 1
def f(n):
    #signature: int -> int
    # returns the value 2*n + 1
    return (succ(double(n)))
def g(n):
    #signature: int -> int
    # returns the value 4*n
    return double(double(n))
def h(n):
    #signature: int -> int
    # returns the value 8*n + 4
    return g(f(n))
def test():
    print(double(2))
    print(succ(2))
    print(f(2))
    print(g(2))
    print(h(2))
test()
