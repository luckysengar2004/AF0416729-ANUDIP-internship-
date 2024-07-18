# Q-Calculating Time in HH:MM:SS format whwn a user give seconds in input

Time = int(input("Enter time in second = "))
if(Time < 0):
    print("enter positive number")
elif(Time < 3600):
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{min} minutes: {sec} second")
else:
    Hour = Time//3600
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{Hour} Hour: {min} min: {sec} seconds")
print("Conversion Sucessful")
