# Infix to postfix/prefix


## Algebraic Expression

- An algebraic expression is a legal combination of **_operands_** and the **_operators_**.
- **_Operand_** is the quantity (unit of data) on which a mathematical operation is performed.
- **_Operand_** may be a variable like `x,y,z` or a constant like `0,1,2,4,5` etc.
- **_Operand_** is a symbol which signifies a mathematical or logical operation between the operands.Example:`+,-,*,/,^` .
- An example of expression as `a+b*c`. 


## Infix, Postfix and Prefix Expression.

- [ ] INFIX: the expressions in which operands surround the operator. e.g `x + y`, `6 * 3` etc, this way of writing the expression is called infix notation.
  - <span style="color:blue">\<Operand></span> <span style="color:red">\<Operator></span> <span style="color:blue">\<Operand></span>
- [ ] POSTFIX: Postfix notation are also known as **_Reverse Polish Notation_** (RPN). They are different from the infix and prefix notations in the sense that in the postfix notation, operator comes after the operands e.g `xy+`, `xyz+*`
  - <span style="color:blue">\<Operand></span><span style="color:blue">\<Operand></span><span style="color:red">\<Operator></span>
- [ ] PREFIX: Prefix notation also known as **_Polish notation_**. In the prefix notation, operator comes before the operands. e.g `+xy`, `*+xyz`
  - <span style="color:red">\<Operator></span><span style="color:blue">\<Operand></span><span style="color:blue">\<Operand></span>


## Operator Priorities

- How do you figure out the operands of an operator ?
  - `a + b * c`
- This is done by assigning operator priorities.
  - `priority(*)` = `priority(/)` > `priority(+)` = `priority(-)`
- When an operand lies between two operators, the operand associates with the operator that has higher priority.


| Symbol | 
|--------|
|   ```(``` or ```)``` |
|   `^` |
|   `*` |
|   `+` or `-` |



## Tie Breaker

- When an operand lines between two operators that have the same priority, the operand associates with the operator on the left.
  - `a + b - c`
  - `a * b / c / d `

## Delimiters

- Sub expression within delimiters is treated as a single operand, independent from the remainder of the expression.
  - `(a + b) * (c - d) / (e - f)`



## WHY??
- Why to use PREFIX and POSTFIX notations when we have simple INFIX notation?
- INFIX notations are not as simple as they seem specially while evaluating them. To evaluate an infix expression we need to consider Operators’ Priority and Associative property
- To solve this problem Precedence or Priority of the operators were defined. Operator precedence governs evaluation order. An operator with higher precedence is applied before an operator with lower precedence.




## Rules for Infix to postfix using stack DS-

1. Scan Expression from Left to Right
2. Print **_OPERANDs_** as the arrive
3. If **_OPERATOR__** arrives & Stack is empty, push this **_operator_** onto the stack.
4. If incoming **_OPERATOR_** has HIGHER precedence than the TOP of the Stack, push it on stack.
5. If incoming **_OPERATOR_** has LOWER precedence than the TOP of the Stack, then POP and print the TOP. Then test the incoming operator against the NEW TOP of stack.
6. If incoming **_OPERATOR_** has EQUAL precedence with TOP of Stack, use ASSOCIATIVITY Rules.
7. For ASSOCIATIVITY of LEFT to RIGHT –
   1. POP and print the TOP of stack, then push the incoming OPERATOR
8. For ASSOCIATIVITY of RIGHT to LEFT –
   1. PUSH incoming **_OPERATOR_** on stack.
9. At the end of Expression, POP & print all  OPERATORS from the stack
10. IF incoming SYMBOL is ‘(‘ PUSH it onto Stack.
11. IF incoming SYMBOL is ‘)’ POP the stack and print OPERATORs till ‘(‘ is found. POP that ‘(‘
12. IF TOP of stack is ‘(‘ PUSH OPERATOR on Stack


## Manual

> Infix : _(A + B) * (C + D)_

| Scanned | Stack | Expression |
|----------|--------|-------------|



## Pseudocode



## infix to postfix

```python


import sys
from collections import deque
 
def prec(c):
 
    if c == '×' or c == '/':
        return 3
    if c == '+' or c == '-':
        return 4
 
    if c == '&':
        return 8

    if c == '^':
        return 9

    if c == '|':
        return 10

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


```




## Example

### 1. Input

```console
(a+b)
(a+b*c)
(r+(s+t))
((r+s)+t)
p+q++r

```

### Output

```console
ab+
abc*+
rst++
rs+t+
Invalid Expression

```

### 2. Input
```console

(A+(B*C))
((A+B)*(Z+X))
((A+T)*((B+(A+C))^(C+D)))

```

### Output

```console

ABC*+
AB+ZX+*
AT+BAC++CD+^*

```