import fibo as fb
import sys
# fb.fib(1000)

# from fibo import *


# def fib(a):
#     print(a)


def main():
    print("-- ch06 --")   
    print(sys.argv)
    fb.fib(int(sys.argv[1]))
    # l = fb.fib2(1000)

if __name__ == "__main__":
    main()