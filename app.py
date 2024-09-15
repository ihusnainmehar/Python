price= 1000000
has_good_credit = True
if has_good_credit:
    downpayment = 0.1*price
    print(f"Down Payment is 10% which is: {downpayment}")
else:
    downpayment = 0.2*price
    print(f"Down Payment is 20% which is: {downpayment}")