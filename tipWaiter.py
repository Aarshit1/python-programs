def total_calc(billAmount, tipPerc):
    total=billAmount*(1+0.01*tipPerc)
    total=round(total,2)
    print(f"please pay ${total}")

total_calc(150,20)