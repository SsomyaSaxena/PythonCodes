a=[]
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    a.append(item)
min=a[0]
for i in range(0,n):
    if  a[i]<min :
          min=a[i]
print("The largest value in the list:",min)    


#OUTPUT:
#Enter the list size : 3
#Enter number at location 0 :
#1
#Enter number at location 1 :
#7
#Enter number at location 2 :
#3
#The largest value in the list: 1
