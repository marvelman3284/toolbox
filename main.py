import sys

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
