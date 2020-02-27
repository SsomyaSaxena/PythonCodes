a=[]
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    a.append(item)
max=0   
for i in range(0,n):
    if  a[i]>max :
          max=a[i]
print("The largest value in the list:",max)    
