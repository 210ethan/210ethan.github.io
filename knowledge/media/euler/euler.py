import math

def bubble():
    
    nums = [1, 3, 2, 7, 6, 8, 10, 15, 13, 100, 93, 91]

    for i in range(1,len(nums)):
        
        for j in range(len(nums)-1):
            
            if nums[j] > nums[j+1]:
                placeholder = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = placeholder
                
    print(nums)


def isprime(i):

    for j in range(2,int(math.sqrt(i))+1):
        if (i % j == 0):
            return False
    return True
        
def is_divisible(num,limit):
    
    for i in range(1,limit):
        if (num % i != 0):
            return False
    return True


def p10_2():
    
    # sieve of erasthones
    # mark 2,3,5,7 as primes
    # eliminate multiples of 2,3,5,7
    # sum all remaining numbers
    
    sum = 17

    for i in range(2,1000):
        if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            pass
        else:
            sum += i
            
    print(sum)

def p10():
    sum = 0
    for i in range(3,2000000,2):
        if isprime(i):
            sum += i
    print(sum+2)


def p6():
    sum_squares = 0
    square_sum = 0
    for i in range(1,101):
        sum_squares += i*i    
    for j in range (1,101):
        square_sum += j
    diff = square_sum*square_sum - sum_squares
    print(diff)


        
def p5():
    i = 1
    while (i>0):
        if is_divisible(i,20):
            print(i)
            break
        else:
            i += 1
            print(i)
    print(i)
                
    
    
    
    
    
    
    
        
        
def p4():
    largest = 0
    for i in range(100,999):
        for j in range(100,999):
            num = str(i*j)
            if (len(num) == 5):
                if (num[0] == num[-1]) and (num[1] == num[-2]):
                    if (int(num) > largest):
                        largest = int(num)
            if(len(num) == 6):
                if (num[0] == num[-1]) and (num[1] == num[-2]) and (num[2] == num[-3]):
                    if (int(num) > largest):
                        largest = int(num)
    print(largest)
    
    
def p3_2():
    n = 600851475143
    i = 2
    while (i * i < n):
        while (n % i == 0):
            n = n / i
        i += 1
    print(n)
    
def p3():            
    num = 600851475143
    ss = int(math.sqrt(num))
    for i in range(ss,1,-1):
        if (num % i == 0) and isprime(i):
            break
    print(i)
    

def p2():
    even_sum = 0
    fib1 = 0
    fib2 = 1
    fib3 = 0
    while (fib3 < 4000000):
        fib3 = fib1 + fib2
        if (fib3 % 2 == 0):
            even_sum += fib3
        fib1 = fib2
        fib2 = fib3
    print(even_sum)
    

def p1():
    multiples = 0
    for i in range (3,1000):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples += i
    print(multiples)

def main():

    bubble()

main()
