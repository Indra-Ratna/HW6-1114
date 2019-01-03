#Indra Ratna
#CS-UY 1114
#27 Oct 2018
#Homework 6
#Problem 1
"""
program 1

q(30,5) returns
10
60
37

program 2 returns 
1
1
1
f!o!o!

program 3 returns 
PPP
"""
def a(s):
    return s.upper() * 3
def b(s):
    return chr(ord(s)+1)
def c(s):
    return s[-1]
def d(s):
    return s.lower() * 3
def e(s):
    print("!" + s + "!")
print(a(b(c(d("Foo")))))
