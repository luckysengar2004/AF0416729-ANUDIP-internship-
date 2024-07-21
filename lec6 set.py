# TO FIND MEMORY ADRRESS IN TUPLE AND SEEING CAN CHNAGE IN Tuple POSSIBLE
'''a= 10,20,30
print(a)
print(id(a))
a=100,200,500,350
print(a)
print(id(a))
print(type(a))'''  #To find the typle of variable.

#CREATION OF SET
a={10,10,20,30}
b={60,50}
print(a) #REMOVE DUPLICATE ELEMENTS
print("---------------------------")
print("to add element in set we use add()")
a.add(50)  #to add element in set
print(a)
print("------------------------")
print("to update element we use update()")
a.update([40,50,60]) # Used to update element
print(a)
print("------------------------")
print("to delete element we use pop() & discard method")
a.pop() #delete random element do not take argument.
print(a)
a.discard(10)   # to delete specific element
print(a)
print("--------------------")
a.clear()  # used to empty the set.
print("SET IS",a)

print("-------------------------------")
#PERFORMING UNION
print(" PERFORMING UNION ")
c =a.union(b)
print(c)