price= input("Enter the Price of House: ")
credit_score = input("Enter your credit Score: ")
if int(credit_score)>=50:
    downpayment = 0.1*price
else:
    downpayment = 0.2*price
print(downpayment)

