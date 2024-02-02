def g_to_ounch(grams):
    ounch=grams*28.3495231
    return ounch
c=100
print(g_to_ounch(c))




def f_to_C(f):
    c=(5/9)*(f-32)
    return c 
print(f_to_C(c))





def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None  

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)
if result:
    num_chickens, num_rabbits = result
    print(f"Number of chickens: {num_chickens}")
    print(f"Number of rabbits: {num_rabbits}")
else:
    print("No solution found.")






def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in input_numbers.split()]
prime_numbers = filter_prime(numbers_list)
print("Original list:", numbers_list)
print("Prime numbers:", prime_numbers)




from itertools import permutations

def print_permutations(input_str):
    perms = permutations(input_str)
    
    print(f"All permutations of '{input_str}':")
    for perm in perms:
        print(''.join(perm))


user_input = input("Enter a string: ")
print_permutations(user_input)





def reverse_words(input_str):
    words = input_str.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_input)

print("Original sentence:", user_input)
print("Reversed sentence:", reversed_sentence)





def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numbers = [1, 2, 3, 4, 3, 5, 6]  # Replace this list with your own

result = has_33(numbers)

print(f"The list {numbers} contains adjacent 3s: {result}")




def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
numbers = [1, 0, 2, 0, 0, 7, 8]  # Replace this list with your own

result = contains_007(numbers)

print(f"The list {numbers} contains '007' in order: {result}")


def volume(rad):
    area=(3/4)*3.14*rad**3
    return area

r=20
print(volume(r))



def is_palindrome(sen):
    if sen==sen[::-1]:
        return True
    else:
        return False
    

print(is_palindrome("madam"))


def histogram(numbers):
    for num in numbers:
        print('*' * num)
list=[3,4,5]
histogram(list)




import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


guess_the_number()