import sys
from collections import deque
 
def prec(c):
    if c == '×' or c == '/':
        return 1
    if c == '+' or c == '-':
        return 2
 
    if c == '&':
        return 3

    if c == '^':
        return 4

    if c == '|':
        return 5

    return sys.maxsize  
def isOperand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
 

def infixToPostfix(infix):
    s = deque()
    postfix = ""

    for c in infix:
        if c == '(':
            s.append(c)
        elif c == ')':
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
 
        elif isOperand(c):
            postfix += c
 
      
        else:
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
 
            s.append(c)

    while s:
        postfix += s.pop()
 
   
    return postfix
 
 
if __name__ == '__main__':
 
    # infix = "A+(B * C(D/E^F)*H"
    infix = input("Enter infix Expression: ")
    postfix = infixToPostfix(infix)

    print(postfix)
 