# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


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
    
def palindrome_fun(n):
    rev_str = n[::-1]
    if(n == rev_str):
        print("Given String is palindrome")
    else:
        print("it is not palindrome")
n = "malayalav"
palindrome_fun(n)


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


def prime_factors(n):
    prime_factors_list = []
    for i in range(2,n+1):
        while n%i == 0:
            prime_factors_list.append(i)
            n = n//i
    print(prime_factors_list)
prime_factors(12)


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




            



            
        
        
        
        

        
            
        
            
    