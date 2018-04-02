# Created April 1st, 2018
# Calculates the fibonacci sequence

FIB_COUNT = 1000


def fib(count):
    # Start the sequence with 1, 1 to save time
    fib_seq = [1, 1]
    for x in range(count):
        # Add the two last numbers together to create the third number
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:-1]

print(fib(FIB_COUNT))
