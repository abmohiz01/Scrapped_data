# def fibinacci(num):
#     if (num == 0 or num == 1):
#         return num
#
#     else:
#         return fibinacci(num - 1) + fibinacci(num - 2)
#
# print (fibinacci(6))
# print (fibinacci(8))
# print (fibinacci(9))
# print (fibinacci(10))
# print (fibinacci(0))
# print (fibinacci(1))
#
a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(fibonacci(i))

# PRINT FACTORIAL5
def factorial(n):
    fact = 1
    assert n >= 0
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    n = int(input("Enter a number :"))
    fact = factorial(n)
    print('Fatctorial of :',n, 'is',fact)
    print(fibonacci(n))
if __name__=='__main__':
    main()



