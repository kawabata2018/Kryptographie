import sys
import numpy as np

def xeuclid(a, b):
    """
    calculate GCD of a & b
    using Euclidean algorithm

    Note:
    a, b must be integer (> 0)
    a must be larger than b
    i.e. a > b > 0
    """
    print()
    print("----------")
    print("Extended Euclidean Algorithm")
    count = 0
    sign = 1
    t = np.array([[1,0], [0,1]])
    aa = a
    bb = b
    print("a:", aa)
    print("b:", bb)
    print("----------")
    print()
    print("count:", count)
    print("coef:\n", t)
    print()
    while True:
        count += 1
        r = a % b
        q = a // b
        a = b
        b = r
        e = np.array([[q, 1], [1, 0]])
        t = np.dot(t, e)
        sign = -sign
        print("count:", count)
        print("coef:\n", t)
        print()
        if b == 0:
            break
    
    x = sign * t[1][1]
    y = -sign * t[0][1]

    print("----------")
    print("gcd(a,b):", a)
    print("{0} = {1} * ({3}) + {2} * ({4})".format(a, aa, bb, x, y))
    print("----------")
    print()

def input_value(count):
    num = input("[" + count + "] Enter an natural number: ")
    try:
        num = int(num)
    except:
        print("Please input an natural number\n")
        return input_value(count)
    else:
        return num

if __name__ == '__main__':
    num1 = input_value("1st")
    num2 = input_value("2nd")
    
    if num1 < num2:
        num1, num2 = num2, num1
    
    xeuclid(num1, num2)
