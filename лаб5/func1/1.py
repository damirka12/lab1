import math
import random
##task 1

def gramToOun(a):
    oun = a * 28.349531
    print(oun)

gramToOun(10)


##task 2

def FarCelConversion(Far):
    c = (5/9) * (Far - 32)
    return c

a = FarCelConversion(10)
print(a)

##task 3 35, 94

def solve(numhead, numleg):
    for i in range(numhead+1):
        j=numhead-1
        if 2*i+4*j == numleg:
            return i,j
    return (None, None)

numleg=94
numhead=35
chicken, rabbit= solve(numhead,numleg)
if chicken == None:
    print('No solution')
else:
    print("Num of chickens: ", chicken)
    print("Num of rabbits: ", rabbit)


##task 4

def check_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n) + 1), 1):
        if n % i == 0: return False
    return True

def filter(list):
    return ' '.join(str(e) for e in list if check_prime(e))

print(filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

## task5

from itertools import permutations

def permutation(a):
    perms = permutations(a)
    for perm in perms:
        print(''.join(perm))

permutation("abc")

##task6

def reverse(a):
    words = a.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

result = reverse('Hello world!')
print(result)


##task7

def has_33(nums):
    print('33' in ''.join(str(e) for e in nums))

has_33([1, 3, 3])
##task 8

def spy_game(nums):
    print('007' in ''.join(str(e) for e in nums if e == 7 or e == 0))

spy_game([1, 2, 4, 0, 0, 7, 5])
##task 9

def volume(rad):
    return 4 * math.pi * pow(rad, 3) / 3

print(volume(5))

##task10

def unique(array):
    ans = list()
    for i in array:
        if i not in ans: ans.append(i)
    return ans

print(unique([3, 1, 2, 3, 6, 4, 1, 2, 3]))


##task11

def palindrome(s):
    return (s == s[::-1])

print(palindrome('qwer'))
print(palindrome('qwwq'))

##tasl12
def histogram(array):
    for i in array:
        print('*' * i)

histogram([4, 9, 7])

##task13

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Take a guess.\n")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break
guess_the_number()


