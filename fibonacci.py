def fibonacci(end):
    x = 0
    n = 1

    sequence = [1]

    for _ in range(end-1):
        sequence.append(x + n)

        n,x = sequence[-1], sequence[-2] # n should be equal to the current sum, and x being the one preceding it

    return sequence

print(fibonacci(10)) # Should print and return the first 10 fibonacci numbers
