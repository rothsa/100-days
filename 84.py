#Write your code below this line 👇
#tests whether n is a multiple of any integer between 2 and the square root of n
import math
def prime_checker(number):
    sqrt = round(number ** (1/2))
    for i in range(2, sqrt+1):
        if number%i == 0:
            print("It's not a prime number")
            break;
        elif i == sqrt:
            print("It's a prime number")
            
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
