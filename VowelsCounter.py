#Create a for loop to count the number of vowels in a string.
vowels = ['a','e','i','o','u']
string = input("Enter a string: ")
count = 0 
for x in string.lower():
    if x in vowels:
        count += 1

print(f"No of Vowels are {count}")