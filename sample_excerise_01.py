# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""
Given a number, find the sum of its digits. Take the number as
an input from the user.
"""

print(sum(list(map(int, input("Enter a number to calculate sum: ").strip()))))


n = 111
sum = 0
while n>=1:
    m = n%10
    sum = sum + m
    n = n//10
print(int(sum))

n = 111
n_str = str(111)
sum = 0
for i in n_str:
    sum += int(i)
print(int(sum))


"""
Given a number, check whether the given number is an
Armstrong number or not. A positive integer is called an
Armstrong number of order n if:
abcd... = an + bn + cn + dn + ...
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
153 is an Armstrong number of order 3.
Inputs from the user will be number and order n
"""

number = input("Enter the number to check for Armstrong: ")
order = int(input("Enter the order: "))

number_list = list(map(int, number.strip()))

armstrong_sum = 0

for numbers in number_list:
    armstrong_sum += numbers ** order

if armstrong_sum == int(number):
    print(True)
else:
    print(False)

n = 153
n_str = str(153)
length_of_n = len(n_str)
sum = 0
for i in n_str:
    sum += pow(int(i),length_of_n)
if(sum == n):
    print("Given number is armstrong")
else:
    print("It is not armstrong")
    
    
"""
Given a string, write a python function to check if it is
palindrome or not.
A string is said to be palindrome if the reverse
of the string is the same as string. For example, “malayalam” is a
palindrome, but “music” is not a palindrome.
"""


# Approach 1: Splicing
def isPalindrome(s: str):
    if s == s[::-1]:
        return True
    else:
        return False


string = input("Enter a string: ")
print(isPalindrome(string))


# Approach 2: Traditional approach
def isPalindrome_traditional(s: str):
    reverse = ""
    for i in s:
        reverse = i + reverse

    if reverse == s:
        return True
    else:
        return False


string = input("Enter a string: ")
print(isPalindrome_traditional(string))
    
def palindrome_fun(n):
    rev_str = n[::-1]
    if(n == rev_str):
        print("Given String is palindrome")
    else:
        print("it is not palindrome")
n = "malayalav"
palindrome_fun(n)


"""
Given an array which may contain duplicates, print all elements
and their frequencies.
"""

frequencies = {}

element_list = ["A", "B", "A", 1, 2, 3, 3, 5, 5, "C", "E", "C", 1]

for element in element_list:
    frequencies[element] = frequencies.get(element, 0) + 1

print(frequencies)



n = [1,2,3,1,2,3,1,2,3,4,5,6,4,5,4]
length_of_n = len(n)
count = 0
unique_list = []
for i in range(len(n)):
    if(n[i] not in n[:i]):
        unique_list.append(n[i])
print(unique_list)
count_of_unique_numbers = []
for i in unique_list:
    count = 0
    for j in n:
        if(i == j):
            count += 1
    count_of_unique_numbers.append(count)
print(count_of_unique_numbers)


  
"""
Given a number n, write a function to print all prime factors of
n. 
For example, if the input number is 12, then output should be
“2 2 3”
"""


def PrimeFactors(n: int):
    prime_factors = []
    i = 2

    for x in range(2, i):
        if n % i == 0:
            prime_factors.append(i)
            for y in range(2, i + 1):
                if x % y == 0:
                    break
    
    print(prime_factors)

PrimeFactors(12)

def prime_factors(n):
    prime_factors_list = []
    for i in range(2,n+1):
        while n%i == 0:
            prime_factors_list.append(i)
            n = n//i
    print(prime_factors_list)
prime_factors(12)


"""
Given two numbers n and r, find the value of nCr (binomial
coefficient: nCr = (n!) / (r! * (n-r)!))
"""

n = int(input("Enter the n value: "))
r = int(input("Enter the r value: "))


# Recursive Method
def factorial_recursive(number: int):
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return 0
    else:
        return number * factorial_recursive(number - 1)


ncr_recursive = int(factorial_recursive(n) / (factorial_recursive(r) * factorial_recursive(n - r)))
print(ncr_recursive)


# Normal Method
def factorial(number: int):
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return 0
    else:
        factorial_num = 1
        for i in range(number, 1, -1):
            factorial_num *= i

    return factorial_num


ncr = int(factorial(n) / (factorial(r) * factorial(n - r)))
print(ncr)
def factorial_fun(n):
    if(n>=1):
        return n * factorial_fun(n-1)
    else:
        return 1

n = 6
r = 5

n_factorial = factorial_fun(n)
r_factorial = factorial_fun(r)
n_minus_r_factorial = factorial_fun(n-r)
divisor = r_factorial * n_minus_r_factorial
dividend = n_factorial
nCr_val = dividend/divisor
print(nCr_val)



"""
Searching: Given a sorted array arr[] of n elements, write a
function to search a given element x in arr[]. Do it using linear
and binary search techniques.
"""

arr = list(map(int, input("Enter the array values: ").strip()))
search_number = int(input("Enter a number to search: "))

arr.sort()


class Searching:

    def __init__(self, number, array):
        self.number = number
        self.array = array

    def linear_search(self):
        """
        Implements Linear Search Algorithm.
        :Inputs:
            - number <int>: Search Number
            - array <list>: Sorted List of Numbers
        :Returns:
            - num <int>: Search Index
        """
        for num in range(len(self.array)):
            if self.number == self.array[num]:
                return f"Number found at index {num}"
                break

    def binary_search(self, first=0, last=0):
        """
        Implements Binary Search Algorithm.
        :Inputs:
            - number <int>: Search Number
            - array <list>: Sorted List of Numbers
            - first <int>: First element in the list
            - last <int>: Last element in the list
        :Returns:
            - num <int>: Search Index
        """
        last = len(self.array) - 1

        while first <= last:

            mid = first + last // 2

            if self.number not in self.array:
                break
            elif self.array[mid] == self.number:
                return f"Number found at index {mid}"
            elif arr[mid] > self.number:
                last = mid - 1
            elif arr[mid] < self.number:
                first = mid + 1

        return "Search number is not found in the list"


search = Searching(number=search_number, array=arr)

print(search.linear_search())
print(search.binary_search())

def linear_search(a,k):
    flag = 0
    for i in a:
        if(k == i):
            flag = 1
    if(flag == 1):
        print("element exist(linearsearch)")
    else:
        print("element not exist(linearsearch)")
            
def binary_search(a,k,low,high):
    if(high>=low):
        mid = (high + low) //2
        if(a[mid] == k):
            return "element exist(binarysearch)"
        elif(k>a[mid]):
            return binary_search(a,k,mid+1,high)
        else:
            return binary_search(a,k,low,mid-1)
    else:
        return "element not exist(binarysearch)"


    
a = [1,2,3,4,5,6,7,8]
key = 0
linear_search(a,key)
print(binary_search(a,key,0,len(a)-1))

line = "bbobnob ******"
print(line.strip("\*"))


"""
Input a text file (containing 1 or more paragraphs of English
text) from the user, parse this file to display the frequency of
occurrence of each word in this text file. Find the 3 most frequent
words as well.
"""


def key_func(k):
    return frequencies[k]


punctuations = [".", ",", "'", "(", ")", "/", "\""]
frequencies = {}

# Read the text file
txt_file = open(file="sample_file.txt", mode="r")

# Split the text files into words
words = [x.lower().split(" ") for x in txt_file.readlines()]

# Convert list of list to normal list
words = [items for x in words for items in x]

# Add frequencies in a Dictionary
for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

# Counting Top 3 Frequent Words
top_3 = sorted(frequencies, key=key_func, reverse=True)[:3]

for top in top_3:
    print(f"{top}: {frequencies[top]}")




            



            
        
        
        
        

        
            
        
            
    
