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

def romanToInt(s):
        
    sum = 0
    dict =  {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    """
    for i in range(1, len(s)):
        if (dict[s[i]] > dict[s[i-1]]):
            value = dict[s[i]] - dict[s[i-1]]
            i += 2
        else:
            value = dict[s[i-1]]
        sum += value
        print("added: ",value)
        print("total: ",sum)
        print("i: ",i)
    print(sum)
     """
    for i in range(len(s)-1):
        # if the next value if larger than current, subtract current from next
        if (dict[s[i]] < dict[s[i+1]]):
            sum -= dict[s[i]]
        else:
            sum += dict[s[i]]   

    print(sum + dict[s[-1]])
    
def longestCommonPrefix(strs):
    
    # check for min length
    minlen = len(strs[0])
    for i in strs:
        if (len(i) < minlen):
            minlen = len(i)
    # only need to check up to the first minlen characters of all strings
    # starting with the first one
    
    # start with first letter of first word
    # loop through entire list and check if they are all the same
        # if not, return empty
        # if yes, loop back and check second lette
    prefix = ""
    for j in range(0,minlen):
        
        # first letters of first word based on j in index
        # only goes up to minlen
        letter = strs[0][j]
        
        # iterate through length of strs list
        for k in range(1,len(strs)):
            # if the jth letter of the kth string
            if (strs[k][j] == letter):
                continue
            else:
                print(prefix)
                return prefix
        prefix += letter
    
    print(prefix)
    return prefix
    

def parentheses(s):
    
    """
    test cases:
    ()
    ((([[{}]])))
    (())[[]]{{}}
        stack = (
    ()(([]{{[]}}[[]])[])
    """
    """
    stack = []

    for i in range(0,len(s)):

        if ((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
            print(s[i])
            stack.append(s[i])
            print("current stack: ", stack)

        if (stack[-1] == "(" and s[i+1] == ")"):
            stack.pop()
            #print("pop: (")

        elif (stack[-1] == "[" and s[i+1] == "]"):
            stack.pop()
            #print("pop: [")

        elif (stack[-1] == "{" and s[+1] == "}"):
            stack.pop()
            #print("pop: {")
        
        #print("End: ",stack)

    if (len(stack) == 0):
        return True
    else:
        return False
    """
    """
    stack = []
    num_pop = 0
    
    if (len(s) % 2 != 0):
        return False

    for i in range(0,len(s)-1):
        
        
        if ((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
            stack.append(s[i])
            print(stack)
            
        if ((s[i] == ")") or (s[i] == "]") or (s[i] == "}")):


        if (len(stack > 0 and stack[-1] == "(" and s[i+1] == ")"):
            stack.pop()
            num_pop += 1

        elif (len(stack) > 0 and stack[-1] == "[" and s[i+1] == "]"):
            stack.pop()
            num_pop += 1

        elif (len(stack) > 0 and stack[-1] == "{" and s[i+1] == "}"):
            stack.pop()
            num_pop += 1
            
        # this fails bc after popping it is zero but still on the close parentheses
        if ((len(stack) == 0) and ((s[i] == ")") or (s[i] == "]") or (s[i] == "}"))):
            print(s[i])
            print("False1")
            return False


    print(stack)
    if ((len(stack) == 0) and (num_pop > 0)):
        print("True")
        return True
    else:
        print("false2")
        return False
    """
    """
    stack = []
    
    if (len(s) % 2 != 0):
        return False

    for i in range(0,len(s)-1):
        
        
        if ((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
            stack.append(s[i])
            print(stack)
        
        if (stack[-1] == "(" and s[i] == ")"):
            stack.pop()
        else:
            print("false1")
            return False

        if (stack[-1] == "[" and s[i] == "]"):
            stack.pop()
        else:
            print("false2")
            return False

        if (stack[-1] == "{" and s[i] == "}"):
            stack.pop()
        else:
            print("false3")
            return False
    
    print("true")
    return True
    """
    
    stack = []
    
    # check every char in string
    for i in range(0,len(s)):
        
        # if opening bracket, push to stack
        if ((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
            stack.append(s[i])

        # if closing bracket, check top of stack
        elif ((s[i] == ")") and (len(stack) > 0) and (stack[-1] == "(")):
            stack.pop()
         
        elif ((s[i] == "]") and (len(stack) > 0) and (stack[-1] == "[")):
            stack.pop()
            
        elif ((s[i] == "}") and (len(stack) > 0) and (stack[-1] == "{")):
            stack.pop()
        
        else:
            print("false1")
            return False
        
    if (len(stack) > 0):
        print("false2")
    else:
        print("True")
        return True
    
def mergeTwoLists(list1,list2):
    
    """
    list1 = 1 2 4
    list2 = 1 3 4
    i = 0
    j = 0
    while (something):
        if (list1[i] <= list2[j]):
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    """
    
    list3 = []
    i = 0
    j = 0
    total_len = len(list1) + len(list2)
    
    if len(list1) == 0:
        list3 = list2
    elif len(list2) == 0:
        list3 = list1
    
    while (len(list3) < total_len):
        if (i < len(list1) and j < len(list2)):
            if (list1[i] <= list2[j]):
                list3.append(list1[i])
                i += 1
            else:
                list3.append(list2[j])
                j += 1
        if (i>=len(list1)):
            list3.extend(list2[j:])
        elif (j>=len(list1)):
            list3.extend(list1[i:])
        print(list3)

    print(list3)

def main():

    #mergeTwoLists([1,2,4,7,9,2000],[1,3,4,11,15,1999])
    mergeTwoLists([0],[])

main()


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

