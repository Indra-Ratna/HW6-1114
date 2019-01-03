#Indra Ratna
#CS-UY 1114
#27 Oct 2018
#Homework 6
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

def test():
    print(rotate("spatula"))
    print(rotates("spatula",0))
    print(rotates("spatula",1))
    print(rotates("spatula",2))
    all_rotations("far")

test()
