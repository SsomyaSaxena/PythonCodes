a=[]
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    a.append(item)
    
sum= 0
for x in range(0,n):
        sum = a[x] +sum
print("SUM:",sum)


#OUTPUT:
# Enter the list size : 5
# Enter number at location 0 :
# 1
# Enter number at location 1 :
# 2
# Enter number at location 2 :
# 3
# Enter number at location 3 :
# 4
# Enter number at location 4 :
# 5
# SUM:15
