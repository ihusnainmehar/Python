name = input('Enter Your Name: ')
if len(name)<3:
    print('Name must be atleast 3 charcters')
elif len(name)>50:
    print('Name can be maximum of 50 characters')
else:
    print('Name looks Good')