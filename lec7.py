#File handling
#Creating file
file=open("Lucky.txt",'w')
file.write(" Todays topic is file handling")
file.close()

#Reading file
file=open("Lucky.txt",'r')
print(file.tell()) # It will tell the postion of data in a file
data=file.read(5)
print(data)
print(file.tell())
file.close()

#seek method - change postion of cursor or  file pointer to read data.
file=open("Lucky.txt",'r')
print(file.tell()) 
file.seek(12)
data=file.read(5)
print(data)
print(file.tell())
file.close()

#Pickle module is used to r/w from binary file. Stores data in same format as in the memory.
import pickle
file=open("pickle.dat",'wb')
li=[10,20,30,40,50]
pickle.dump(li,file)
file.close()

#pickle
import pickle
file=open("pickle.dat",'rb')
data=pickle.load(file)
print(data)
file.close()

#Csv file
import csv
f=open("lucky.csv",'a',newline="")
wo=csv.writer(f)
data=[["a","b","c","d"],[16,15,14,13],[12,52,46,90],[36,52,75,94]]
wo.writerows(data)
f=open("lucky.csv",'r')
re=csv.reader(f)
li=list(re)
for i in li:
    print(i)
f.close()


