#####################################################################
# Version: 1.1
# Author: Bevlin Reddy, databreddy@gmail.com 
# Description: Using modulus we will receive a list of remainers. The 
# objective is to determine the orginal number.
# This seems to be an ideal problem for computation mathematics.
# This may be the Chinese remainder problem.
# Updated: 19-Nov-23
#####################################################################

import math

# =================================================================
# generate a sequence of divisors and remainders
def find_remainder():

    num = int(input("Enter a number: "))

    for i in range(2, num):
        # printing factors will simplify the task
        rem = num%i
        if rem != 0:            
            print(num, "%", i, "=", num%i)
    
    return  

# =================================================================
def find_number(divisor1, remainder1, divisor2, remainder2, divisor3, remainder3):
    
    divisor1_list = []
    divisor2_list = []
    divisor3_list = []
    
    for i in range(1,400):
        # print(divisor1*i+remainder1, divisor2*i+remainder2)
        divisor1_list.append(divisor1*i+remainder1)
        divisor2_list.append(divisor2*i+remainder2)
        divisor3_list.append(divisor3*i+remainder3)
    
    common_elements = list(set(divisor1_list) & \
        set(divisor2_list) & \
            set(divisor3_list))

    common_elements.sort()
    print(common_elements)
    
find_remainder()

# =================================================================

print(">>>>>>>>")
divisor1a = int(input("divisor1: "))
remainder1a = int(input("remainder1: "))
divisor2a = int(input("divisor2: "))
remainer2a = int(input("remainder2: "))
divisor3a = int(input("divisor3: "))
remainer3a = int(input("remainder3: "))
                       
find_number(divisor1a, remainder1a, divisor2a, remainer2a, divisor3a, remainer3a)

# =================================================================
# The above is NOT brute force and somewhat an algorithm.
# So, now I need to make this algorithm better.

# conjecture
# if i > num/2 then i+remainder = num
# but I would know if i  > num/2

# (num - rem)%i = 0
    