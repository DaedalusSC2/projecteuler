"""

Euler problem #001:
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    
    Find the sum of all multiples of 3 or 5 below 1000.
    
    Approach:
        - use the range 1 to 999
        - filter it with the lambda-function as stated in the problem
        - sum up the result of the filtering
        - print out the sum.
        x no list conversion needed, because we only want the result.
    
    Answer: 233168.

"""

print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))
