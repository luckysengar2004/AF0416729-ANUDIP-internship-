#-------------------ASSIGNMENT-------------------------------------
#Q-1- Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    return a / b
num1 = 10
num2 = 2
result = div(num1, num2)
print("The result of the division is:", result)

#Q-2- Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number
def square(a):
    return a*a
num1 = 10
result = square(num1)
print("The result of the square is:", result)

#Q-3- Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
max_number = max(random_numbers)
min_number = min(random_numbers)
print("The random numbers are:", random_numbers)
print("The maximum number is:", max_number)
print("The minimum number is:", min_number)

#Q-4- Accept a name from the user and display that in lower case using lower()function
str=str(input("Enter a string:-"))
str=str.lower()
print(str)



print("---------------------------Assignment------------------")

#Q-1- Write a Python program to count the occurrences of each word in a given sentence
str1 = " To change the overall look of your document. To change the lookavailable in the gallery "
words = str.split()
word_counts = {}
for word in words:
    word = word.strip('.,')  # Remove punctuation
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word, count in word_counts.items():
    print(f"{word}: {count}")

#Q-2- Write a Python program to remove a newline in Python
Str = "\nBest \nDeeptech \nPython \nTraining\n"
string_without_newlines = str.replace('\n', ' ')
string_without_newlines = string_without_newlines.strip()
print("String without newlines:", string_without_newlines)

#Q-3- Write a Python program to reverse words in a string
Str = "Deeptech Python Training"
words = str.split()
reversed_words = words[::-1]
reversed_string = ' '.join(reversed_words)
print("Reversed string:", reversed_string)

# Q-4- Write a Python program to count and display the vowels of a given text
string = "Welcome to python Training"
string = string.lower()
vowels = "aeiou"
vowel_count = {vowel: 0 for vowel in vowels}
for char in string:
    if char in vowels:
        vowel_count[char] += 1
for vowel, count in vowel_count.items():
    print(f"'{vowel}': {count}")
vowels_in_string = [char for char in string if char in vowels]
print("Vowels in the string:", ''.join(vowels_in_string))

print("------------Assignment------------------------")
# Q-1- Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve”
def count_characters(input_string):
    chars = digits = symbols = 0

    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return chars, digits, symbols

input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_characters(input_string)
print(f"Chars = {chars} Digits = {digits} Symbols = {symbols}")

# Q-3- Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
def count_character_types(input_string):
    uppercase = lowercase = digits = special = 0

    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():
            special += 1

    return uppercase, lowercase, digits, special

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, digits, special = count_character_types(input_string)
print(f"UpperCase: {uppercase}")
print(f"LowerCase: {lowercase}")
print(f"NumberCase: {digits}")
print(f"SpecialCase: {special}")

# Q-4- Write a Python Count vowels in a string
#input= “Welcome to Python Assignment”
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

input_string = "Welcome to Python Assignment"
vowel_count = count_vowels(input_string)
print(f"Total vowels are: {vowel_count}")

