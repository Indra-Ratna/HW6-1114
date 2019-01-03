#Indra Ratna
#CS-UY 1114
#27 Oct 2018
#Homework 6

#Problem 2
def print_top(offset):
    #signature: int -> NoneType
    print(offset*" "+'^')
def print_middle(offset, width):
    #signature: int, int -> NoneType
    print(offset * ' ' + '/' + width * ' ' + '\\')
def print_bottom(offset, width):
    #signature: int, int, -> NoneType
    print(offset*" "+width*"-")
def print_triangle():
    print_top(4)
    print_middle(3,1)
    print_middle(2,3)
    print_middle(1,5)
    print_bottom(1,7)

#Problem 3
def rotate(s):
    """
    sig: str -> str
    Return the rotation of the given string
    rotate("spatula") == "patulas"
    """
    newString=""
    n=1
    for letter in range (n,len(s)):
        newString += s[letter]
    for letter in range(n):
        newString+=s[letter]
    return newString

def rotates(s,n):
    newString=""
    if(n==1):
        return rotate(s)
    else:
        for letter in range(n,len(s)):
            newString+=s[letter]
        for letter in range(n):
            newString+=s[letter]
    return newString

def all_rotations(s):
    acc = ""
    for combos in range (len(s)):
        acc+=((rotates(s,combos)+"\n"))
    print (acc)

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

#Problem 5

def sum_range(start_num, end_num):
    """
    signature: int, int -> int
    precondition: end_num >= start_num
    Returns the sum of all numbers between start_num
    and end_num
    """

    sum = 0
    for value in range(start_num, end_num+1):
        sum+=value
    return sum

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
    print_triangle()
    
    print(rotate("spatula"))
    print(rotates("spatula",0))
    print(rotates("spatula",1))
    print(rotates("spatula",2))
    all_rotations("far")

    print(double(2))
    print(succ(2))
    print(f(2))
    print(g(2))
    print(h(2))

    print(sum_range(5,5))
    print(sum_range(-4,4))
    print(sum_range(0,10))
    print(sum_range(1,11))
    
    print(count_doubled("fof"))
    print(count_doubled("foof"))
    print(count_doubled("fooff"))
    print(count_doubled("foooff"))

    
test()



