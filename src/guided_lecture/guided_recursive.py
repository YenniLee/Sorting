def my_recursion(n):
    print(n)
    if n == 3:
        return
    else:
        my_recursion(n+1)
        my_recursion(n+1)


my_recursion(1)

# Fibonacci 

# 0, 1 - Base = if we solve recursively move towards it
# 
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 
#  10th fib number?

# 9th fib + 8th fib 
# 
# 9th fib is?
# 
# 8th + 7th
# 
# base case is ...? 1 and 0 
# 
def recursive_fib(n):
    # base case
    # test for negatives (TOOO)
    # if n is 0
    if n == 0:
        return 0 
    # return 0
    # if n is 1
    if n == 1:
        return 1
    # return 1
    
    # if we're not on the base case 
    # return recursion of n-1 and n-2
    n_minus_1 = recursive_fib(n-1)
    n_minus_2 = recursive_fib(n-2) 
    return n_minus_1 + n_minus_2

print(recursive_fib(5))