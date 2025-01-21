print("welcome to domino's pizza")
bill=0
size=input("what size would you like to have S, M, L")
pepperoni=input("would you like to have pepperoni? Y or N?")
cheese=input("do you want extra cheese? Y or N?")

if size=="S":
    bill=15
    if pepperoni=="Y":
        bill+=2
    if cheese=="Y":
        bill+=1    
    else:
        bill=15    
elif size=="M":
    bill=20
    if pepperoni=="Y":
        bill+=3
    if cheese=="Y":
        bill+=1    
    else:
        bill=20
else :
    size=="L"
    bill=25
    if pepperoni=="Y":
        bill+=3
    if cheese=="Y":
        bill+=1    
    else:
        bill=25

print(f"your final bill is {bill}")
