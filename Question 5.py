i=0
total = 0
while i<=5:
    x=float(input("Enter the deposit amount: Rs."))
    total = total + x
    if x == 0:
        i=6
    else:
        i=4
if total >= 10000:
    print("Premium Customer")
else:
    print("Regular Customer") 
print("Total deposit amount is: Rs.",total)
