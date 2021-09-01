# Fibonacci

Fibonacci, also known as **_Leonardo Bonacci_**, **_Leonardo of Pisa_**, or Leonardo Bigollo Pisano, was an Italian mathematician from the Republic of Pisa, considered to be "the most talented Western mathematician of the Middle Ages"


Here is a longer list:

```console

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811

```

Makes A Spiral

![fibonacci](https://www.mathsisfun.com/numbers/images/fibonacci-spiral.svg)

Do you see how the squares fit neatly together?
For example 5 and 8 make 13, 8 and 13 make 21, and so on.

![fib](https://www.mathsisfun.com/numbers/images/sunflower.jpg)


## PHI or FIE -> The Golden RATIO

![phi](https://www.quickanddirtytips.com/sites/default/files/images/1649/golden-ratio-shell.png)

So we can write the rule:

The Rule is `xn` = `xn − 1 +  xn −2`

where:

`xn` is term number `n`
`xn−1` is the previous term `(n−1)`
`xn−2` is the term before that `(n−2)`



## Fibonacci

```python

def fibonacci(x):
    a = 0
    b = 1
    print(a,end="")
    print(' ',b,end="")
    for i in range(2,x):
        c = a + b
        a = b
        b = c
        print(' ',c,end="")
    print("")

fibonacci(10)


```



### Recursion

```python


def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

for x in range(10):
    print(fibonacci(x))



```