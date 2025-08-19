def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1) + fib(n-2)

hash_map = {0:0,1:1}
def dp_fib(n):
    if n in hash_map:
        return hash_map[n]
    hash_map[n] = dp_fib(n-1) + dp_fib(n-2)
    return hash_map[n]

def new_dp_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return c

import datetime
start = datetime.datetime.now()
print(new_dp_fib(50000))
end = datetime.datetime.now()

print(end-start)