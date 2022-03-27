def fibonacci(n):
    x, y = 0, 1

    num = 1

    for _ in range(n-1):
        last_sum = num
        num = x + y

        y,x = num, last_sum

    return num

print(fibonacci(6)) # should return the 6th fibonacci number
