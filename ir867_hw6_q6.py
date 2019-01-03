#Indra Ratna
#CS-UY 1114
#27 Oct 2018
#Homework 6
#Problem 6

def count_doubled(s):
    """
    signautre: str -> int
    Returns the number of times that s
    contains a doubled character
    """
    double = 0
    DoubleLetter = 0
    element = 1
    while element < len(s):
        if s[DoubleLetter]==s[element]:
            double+=1
        DoubleLetter = element
        element+=1
    return double

def test():
    print(count_doubled("fof"))
    print(count_doubled("foof"))
    print(count_doubled("fooff"))
    print(count_doubled("foooff"))
test()
