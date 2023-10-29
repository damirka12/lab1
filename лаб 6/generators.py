# Create a generator that generates the squares of numbers up to some number N.

def squarGen(N):
    i = 1
    while(i <= N):
        yield i**2
        i+=1

for i in squarGen(5):
    print(i)


#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def evenNumbers(n):
    i = 0
    while(i<=n):
        if(i%2==0):
            yield i
        i+=1



n = int(input("Введи n\n"))
g = evenNumbers(n)
print(list(g))


#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divis(n):
    divtf=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            divtf.append(i)
    yield divtf

a=divis(int(input("Введи а\n")))
print(*next(a))

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def pow2(a,b):
    for i in range(a,b):
        yield i**2

c = pow2(6,9)
for i in range(9-6):
    print(next(c))


#Implement a generator that returns all numbers from (n) down to 0.

def down(n):
    for i in reversed(range(n)):
        yield i

d=down(5)
for i in range (5):
    print(next(d))