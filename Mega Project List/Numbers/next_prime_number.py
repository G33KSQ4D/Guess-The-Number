# Created April 1st, 2018 (Happy April Fools - No easter eggs here sorry, maybe next time)

# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

def is_prime(n):
    """ Returns whether a number is prime or not using modulus """

    # range(<# Inclusive >, <# Exclusive>) not including # 1 therefore starting at 2
    for x in range(2, n):
        if n % x == 0:
            return False
    # If it reaches this point it means it's a prime
    return True

def clr_scr():
    print("\n" * 100)

# Kind of cheated with this by making a list of primes in advanced (First 10000)
# Doubt user will ask for more than 10000 primes

prime_numbers = []
max_num = 10000
for x in range(2, max_num):
    max_num = 10000
    if is_prime(x):
        prime_numbers.append(x)

# At this point I've got a list of 10, 000 prime numbers

print("Welcome to find the next prime number!\n\n")

# Printing prime numbers until user enter q to stop
prime_numbers_index = 0
while input("Press anything to see more prime numbers\nEnter 'q' to quit\n").lower() != 'q':
    clr_scr()
    print("Prime numbers: " + str(prime_numbers[0:prime_numbers_index]))
    prime_numbers_index += 1
