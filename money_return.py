total=50
paid_amt=float(input("The total amount is $50. Please pay up : $"))
if paid_amt==50:
    print("thank you")
elif paid_amt<50:
    insufficient=50-paid_amt
    print("the bill is $50, pay $",insufficient, "more")
elif paid_amt>50:
    change=paid_amt-50
    print("thank you here is your $",change, "back")
else:
    print("pay $50")