#File handling assignment
# Q-1-  Write a program to count the occurrence of word "INDIA" in a text file India.txt.
file=open("India.txt",'w')
file.write("India is my country. India is my pride. India , India.")
file.close()
file=open("India.txt",'r')
data=file.read()
print(data)
words = data.split()
counts = 0
for word in words:
    word = word.strip('.,')  # Remove punctuation
    if word =="India":
        counts =counts+1
print(f"{word}: {counts}")
file.close()

# Q-2- Write the program to count and display the lines starting with "T" in a text file story.txt
# Write content to the file
file = open("story.txt", 'w')
file.write("Hello Lucky, welcome to the python class.\n")
file.write("Today is sunny day.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Today,we are learning pyhton.\n")
file.write("Today, we are learning File handling topic in python.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()
# Open the file in read mode
file = open("story.txt", 'r')
# Read the content of the file
count = 0
content = file.readlines()
# Iterate over each line in the file content
for line in content:
    if line[0] == 'T':
        print(line, end='')  # Print the line that starts with 'T'
        count += 1
# Print the count of lines starting with 'T'
print("Number of lines starting with 'T':", count)
# Close the file
file.close()

# Q-3- Write a program to count the numbers of vowels and constants in a file "Myfile.txt".
file=open("Myfile.txt",'w')
file.write("aeiou aeiou the")
file.close()
file=open("Myfile.txt",'r')
data=file.read()
print(data)
vowels = "aeiouAEIOU"
count = 0
counts = 0
for char in data:
    data = data.strip("., ")
    if char in vowels:
        count+=1
    elif char ==" ":
        counts+=0
    else:
        counts+=1
print(f"Total vowels are: {count}")
print(f"Total constants are: {counts}")
file.close()

# Q-4- Write a program to count and display number of words starting with "I" in a file word.txt
# Write content to the file
file = open("file.txt", 'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello Lucky, welcome.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()
# Open the file in read mode
file = open('file.txt', 'r')
# Read the content of the file
data = file.read()
# Split the content into words
words = data.split()
# Initialize the counter for words starting with 'i'
count_i = 0
# Iterate over the words and count those starting with 'i'
for word in words:
    if word[0].lower() == 'i':
        count_i += 1
        print(word)
# Print the count
print("Number of words starting with 'i':", count_i)
# Close the file
file.close()

#Q-5-Write a program to display thw word having more than 5 words in a text file notes.txt.
# Write content to the file
file = open("notes.txt", 'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello python .\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()
# Open the file in read mode
file = open('notes.txt', 'r')
# Read the content of the file
data = file.readlines()
# Iterate over each line in the file content
for line in data:
    # Split the line into words and check if it has more than 5 words
    if len(line.split()) > 5:
        print(line.strip())
# Close the file
file.close()

#Q-  WAP to create a binary file "stu.dat" and enter students roll number name and marks till user wants
import pickle
file=open("Stu.dat","wb")

while True:
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
                
    student = {
        'roll_number': roll_number,
        'name': name,
        'marks': marks
        }
            
            # Serialize the student dictionary and write it to the binary file
    pickle.dump(student, file)
            
    more = input("Do you want to enter another record? (yes/no): ").strip().lower()
    if more != 'yes':
        break
file.close()


# Q-write a program to read a binary file storage display the record of student having marks greater than 81
fil=open("Stu.dat","rb")
while True:
    student = pickle.load(fil)
    if student['marks'] > 81:
        print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Marks: {student['marks']}")
    break
   
fil.close()
