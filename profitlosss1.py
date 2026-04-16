actual_cost=float(input("enter the actual cost of the item "))
sale_cost=float(input("enter the sale cost of the item "))

if(sale_cost>actual_cost):
    cost = sale_cost-actual_cost
    print("total profit={0}".format(cost))
    if(cost>10):
        print("give in rent")
else:
    print("no profit")