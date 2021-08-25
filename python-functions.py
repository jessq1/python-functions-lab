def sum_to(n):
    total = 0
    while n>0:
        total += n
        n -= 1
    return total

def largest(arr):
    max = arr[0]
    for n in arr:
        if n>max:
            max = n
    return max

def occurances(tx1,tx2):
    return tx1.count(tx2)

def product(*args):
    prod = 1
    for arg in args: 
        prod *= arg
    return prod

