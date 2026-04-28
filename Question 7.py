print("Enter the electricity consumption of 3 months below!")
i=1
tot=0
while i<=3:
    x=int(input("Enter: Units."))
    tot=tot + x
    i=i+1


if tot>300:
    print("High Usage")
else:
    print("Regular/Normal Usage")

