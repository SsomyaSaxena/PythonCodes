a=[]
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    a.append(item)
tot = 1
for x in range(0,n):
    tot *= a[x]
print("The multiplied value is:",tot)


#OUTPUT:
#Enter the list size : 3
#Enter number at location 0 :
#1
#Enter number at location 1 :
#2
#Enter number at location 2 :
#4
#The multiplied value is: 8
