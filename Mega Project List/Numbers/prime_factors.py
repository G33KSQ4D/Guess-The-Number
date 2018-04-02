# Created April 1st, 2018 (Happy April Fools - No easter eggs here sorry, maybe next time)

# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.


def is_prime(n):
    """ Returns whether a number is prime or not using modulus """

    # range(<# Inclusive >, <# Exclusive>) not including # 1 therefore starting at 2
    for x in range(2, n):
        if n % x == 0:
            return False
    # If it reaches this point it means it's a prime
    return True


def find_prime_factors(max_num):
    """ Find all prime factors until a certain number (Exclusive) """
    prime_factors = []
    for x in range(2, max_num):
        # Checks to see if max_num is divisible by a number of that number and if that number is prime
        if max_num % x == 0 and is_prime(x):
            prime_factors.append(x)
    return prime_factors

# You can change this value to see prime factors for a certain number
num = 1337
print(find_prime_factors(num))
