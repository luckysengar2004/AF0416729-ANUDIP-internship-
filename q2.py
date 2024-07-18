# UNDERSTANDING ELIF USING A PROBLEM - CALCULATING PROFIT AND LOSS BASED ON COST AND SELLING PRICE.
cp = int(input("Enter cost price (in rs) - "))
sp = int(input("Enter selling price (on rs) - "))
if(cp < 0):
    print(" Inavlid cost price ")
elif(sp < 0):
    print(" Inavlid selling price ")
else:
    if(sp > cp):
        print("Profit: Rs" , (sp-cp))
    elif(sp > cp):
        print("Loss: Rs" , (cp-sp))
    else:
        print(" No profit no loss ")
