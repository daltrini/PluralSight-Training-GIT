'''Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that
divides evenly into another number. For example, 13 is a
divisor of 26 because 26 / 13 has no remainder.)

Usage:
    python divisible.py <INTEGER>
'''

import sys

def divisors(x):
    '''Creates a list with all numbers that are divisors of an integer
    Args:
        x: The number for which the divisors will be calculated

    Returns:
        List of all divisors

    Raises:
        ValueError: If x is not integer
    '''

    divisors = []
    # if x.is_integer() != True:
    #     raise ValueError(f"cannot compute divisors of non integer value {x}")
    # print('\n==>DEBUG: Enter divisors function with  value:', x)
    for i in range(1,x+1):
        # print('==>DEBUG: Potential divisor:', i)
        # print(f"result of x%i '{x%i}'")
        if x%i == 0:
            divisors.append(i)
    return divisors

# New comment for GIT tracking

if __name__ == '__main__':
    # print('\n==>DEBUG: Enter main with INTEGER value:', sys.argv[1])
    entry = int(sys.argv[1])
    div = divisors(entry)
    print("List of divisors: ", div)
    if len(div) == 2:
        print(f"'{sys.argv[1]}' is a prime number")
    else:
        print(f"'{sys.argv[1]}' is a NOT prime number")
