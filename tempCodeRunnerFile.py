print("Number between 100 to 1000 which are even and divisible by 3")
count = 0
for i in range(100,1000):
    if(i%2==0 and i%3 ==0):
        count += 1
print("total numbers are - ",count,end =" ," )