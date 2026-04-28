i=1
count=0
while i<=5:
    x=int(input("Enter the stock quantity: Units."))
    if x<10:
        count=count+1
        i=i+1
    else:
        i=i+1
print("items less than 10 stock: ", count)