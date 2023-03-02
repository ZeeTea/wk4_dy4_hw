#Please answer 3 codewars problems and measure your answers Time Complexity.

#In order to submit, you can copy 
#your answers to a python file and comment above it 
#with the time complexity that you came up with and a brief explanation of 
#how you got to that complexity.

#1 CodeWars Question

# Vowel count

#The time complexity is O(n) because it goes through each character of a string once.

# This code runs by going through the string containing vowels then, in count it equals 0 
#so in the for loop it checks if the letter contains a vowel.

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

sentence = "Hello, how are you?"

print(get_count(sentence))

#2 Codewars Question

# Sum of Positives

# Time Complexity should be O(n*2) because this pseudocode deals with taking positive numbers only in the array
# and adds them together to get a sum.

# The way this code will work is that it will go through the for loop and look through the list from begining
# of the list all the way to the end and take out all positive numbers. The way it knows it needs to look for positive
# numbers is that if the number is not greater than 0 the it knows not to add them
# and afterwards when it has found the positive numbers it adds them together to give
# you the sum then it ends.

def positive_sum(arr):

    sum = 0
    
    for num in arr:

        if num > 0:
            sum += num

    return sum

arr = [-1, 2, -3, 8]
result = positive_sum(arr)
print(result)

#3 Codewars Question

# Highest to Lowest

#The time complexity is O(n log n) because of the max and min functions which uses the sorting. 

#This code uses the min and max function to go through the string of numbers in the input and 
# converts it to a list of integers using a list. and it returns the string containing the highest 
# and lowest values in the the given string of numbers

def high_and_low(numbers):

    num_list = [int(num) for num in numbers.split()]

    highest = max(num_list)
    lowest = min(num_list)

    return f"{highest} {lowest}"

numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
result = high_and_low(numbers)