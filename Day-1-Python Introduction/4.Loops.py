"""Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print i^2.
"""

def square(n):
    "This function prints square of each number less than n and greater than zero."
    for i in range(n):
        print(i * i)


if __name__ == '__main__':
    n = int(input())
    square(n)
