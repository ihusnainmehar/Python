weight = input("Enter Weight: ")
unit = input("(L)bs or (K)g: ")
if unit.upper == "L":
    new_weight = int(weight)*0.45
    print(f'You are {new_weight} kilos')
elif unit.upper=="K":
    new_weight = int(weight)/0.45
    print(f'You are {new_weight} pounds')
else:
    print("Please Specify unit of Weight")
