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


print_triangle()
