# Created April 1st, 2018 (Happy April Fools - No easter eggs here sorry, maybe next time)

# "Fibonacci Sequence - Enter a number and have the program generate
# the Fibonacci sequence to that number or to the Nth number."

FIB_COUNT = 1000


def fib(count):
    """ Find all fibonacci numbers until a certain count """
    # Start the sequence with 1, 1 to save time
    fib_seq = [1, 1]
    for x in range(count):
        # Add the two last numbers together to create the third number
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:-1]

print(fib(FIB_COUNT))
