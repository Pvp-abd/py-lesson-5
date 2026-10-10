def factorial (num):
    if num == 0 or num == 1:
        return 1 
    else :
        return num*factorial(num-1)
number=int(input("enter you number"))
print ("factorial of this number is",factorial(number))