i=1
cal=0
while i<=5:
    x=float(input("Enter the price: Rs."))
    cal=cal+x
    i=i+1
print("Your total price: Rs.",cal)
if cal>5000:
    y=(cal/100)*20
    cal=cal-y
    print("Price after discount: Rs.",cal)
else:
    print("No discounts")
