from ast import If
from math import remainder
from operator import truediv
from pickle import FALSE, TRUE
from re import X


print("hello world")
last_name='samuel'
first_name ='abenezer'
age=54
print(first_name,last_name,age)

a=7
b=3
x=a+b
sub=a-b
product=a*b
remainder=a%b
floordiviton=b//a
exp=b**a



print('the totale number is',x,sub)

print('the differnce is',sub )
print('the product is',product)

print('the remainder is',remainder)

print('the floordivition is',floordiviton)

print('the expontial number is ',exp)
print('the power is',exp)


# data taype
#print('mister x') this is string
#age=35 this is intger
#gravity=6.84 this is float

gravity=6.6
mass=64

weight=mass*gravity

print(weight)
#area=(pi*r*) pi= 3.14

r=10
pi=3.14

area=pi*r*r

print('the area is',area)

#oprators

# artimatic operator
#example +,-,/,*,%,//,**

print(3+8)
print(6-4)
print(40/5)
print(10%3)
print(7//4)
print(3**3)

#assignment operator

gravity=6.86
weight=64.8 # assignment operator is (=)

#logical operator 
#example and,or
 
#compartion operator 
# example ==,<,>,<=,>=,!=

print(6>5)
print(2>1)
print(6<4)
print(4<=3)
print(6<=6)
print(3=='3')

print(3 != 3)
print(3**4)

print(2 is 2)

print(3<5 and 5==5)#true + true is true 

print(64>24 and 12<2)#true + false is false

print(2==6 and 4>1)#false + false is false 


print(3<5 or 5==5)#true + true is true

print(64>24 or 12<2)#true + false is true

print(2==6 or 4>1)#false + false is false 

print(not 3==3)

#list
#list methods:append,extend,slice,sorted

numbers=[1, 2, 3, 4, 5, 6]
names=['abenezer', 'natan', 'yordi', 'sami']
fruits=['mango', 'banana', 'apple', 'avocado']
countris=['etiohipia', 'polnd', 'sewden', 'finland']

numbers=[1, 2, 3, 4, 5, 6]

print(numbers[2])

print(numbers[-2])

shoplist=['banana', 'mango', 'apple', 'strobery']
print(shoplist)
shoplist[2] = 'papaya'
print(shoplist)

list_one = [1,2,3]
list_two = [4,5,6]

list= list_one+list_two
print(list)
#append method add one list 

num=[1,2,3,4]
print(len(num))

num.append(5)
num.append(68/6)
print(num)

#extend method add or more list

num=[1,2,3,4]
num.extend([5,6,7,8,9])
print(num)
#insert method add miss value

num.insert(8,0)
print(num)

#slice

fruits=['mango', 'banana', 'apple', 'avocado']
print(fruits[1:3])

print(fruits[0:3])
print(fruits[::-1])# basic concepet

fruits.sort()
print(fruits)# alphabtic order "sort"

#conditional "elif", "else", "if"
 
x=5
if x>0:
    print('the number is greater than 0')
elif x==0:
    print('the number is zero')
else:
    print('the number is negative')
    
x=-3
if x>0:
    print('the number is greater than 0')
elif x==0:
    print('the number is zero')
else:
    print('the number is negative')
    
    
x=0
if x>0:
    print('the number is greater than 0')
elif x==0:
    print('the number is zero')
else:
    print('the number is negative')
    
weather ='rainy'
        
if weather =='raniy':
    print('please,take your raincoat.')
elif weather == 'foggy':
    print('the day seems very foggy')
else:
    print('we dont need raincoan.')
    
#loops
#example "for" , "while"
'''
for x in range (4):
    print(x)
for x in range (4,13,):
    print(x)
for x in range (4,13,2):
    print(x)
'''     
all_evens = 0
all_odds =0 

for x in range (101):
   if  x % 2 == 0: # dont miss it
    all_evens = all_evens + x
    print('evens',x)
else:
    all_odds = all_odds + x
    print('odds',x)
    
print('All evens:',all_evens,'All odds:',all_odds)

nums=[1,2,3,4,5]
new_nums=[]
for num in nums:
    new_nums.append(num ** 2)
    
print(new_nums)

countries=['etiohipia', 'polnd', 'sewden', 'finland']
print(countries.reverse())

new_countries = []
for country in countries:
    new_countries.append(country.upper())#this method use change small to capital
    
print(new_countries)
    
  #while loop
'''
x = 0
while x < 6:
    print(x)
    x = x + 1
'''
for i in range (6,0,-1):
    print(i)

countries=['etiohipia', 'polnd', 'sewden', 'finland']
new_countries = []
for country in countries:
    new_countries.append(country.upper())
    
print(new_countries[::-1])

#function

def my_name ():
    first_name = 'abenezer'
    last_name ='samuel'
    full_name = first_name + ' ' + last_name
    return full_name

print(my_name())

def my_name (first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name

print(my_name('natan','samuel'))
print(my_name('yabsera','samuel'))

def calculate_sum_of_even(n):
    all_evens = 0
    for x in range (n+1):
        if  x % 2 == 0: # dont miss it
             all_evens = all_evens + x
    return all_evens

print(calculate_sum_of_even(100))

#factoriyal

def factoriyal(n):
    f = 1
    for i in range (1, n+1):#print(f'{f} * {i} = {f * i}') try it see the result
        f = f * i
    return f
    
print(factoriyal(6))
    
def add_two_nums(a,b):
    total = a + b
    return total

print(add_two_nums(90,10))





def product_two_nums(a,b):
    total = a * b
    return total
print(product_two_nums(80,20))

def square_of_value(a):
    total = a ** b
    return total 
print(square_of_value(3))

print(6<4)
print(3=='3')

print(3 != 3)

names=['abenezer', 'natan', 'yordi', 'sami']
nums.append(4)

print(names)
