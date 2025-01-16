ap = int(input("Enter the actual Price of the product: "))
sp = int(input("Enter the Selling Price of the product: "))

if sp > ap:
    profit = sp - ap
    print(f"Apnar Profit : {profit}")
    
else:
    loss = ap - sp
    print(f"Apnar Loss : {loss}")