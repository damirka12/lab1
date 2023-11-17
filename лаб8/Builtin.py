from functools import reduce
from time import sleep
import math, time
print('task1')
list=[range(1,11)]
r1=reduce((lambda x,y: x*y), list)
print(r1)
print('task2')
str1='I am Damir Alimzhan, I am KBTU student letttt goooOoOoOoOo'
def nums_of_occur(s):
    small_case=0
    upper_case=0
    for letter in s:
        if letter.isupper():
            upper_case+=1
        elif letter.islower():
            small_case+=1
    return upper_case, small_case
x,y=nums_of_occur(str1)
print(x,y)
print('task3')
str2='abba'
def pal_or_not(s):
    s1=s[::1]
    if s1==s:
        return 'palindrome'
    else:
        return 'shit no'
r3=pal_or_not(str2)
print(r3)
print('task4')
def sqrt_after_delay(number, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(number)
    return result
number = 25100
delay = 2123
result = sqrt_after_delay(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}.")
print('task5')
my_tuple=(True, True)
if all(my_tuple):
    print('All are true')
else:
    print('Not at all')