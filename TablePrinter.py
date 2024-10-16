#Write a program that prints the multiplication table of a number entered by the user using a for loop.

number = int(input("Enter a Number: "))
for x in range(1,11):
    table = number*x
    print(f"{number}*{x} = {table}")
    x+=1