a=[]
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    a.append(item)

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

#OUTPUT:
'''
Enter the list size : 5
Enter number at location 0 :
1
Enter number at location 1 :
2
Enter number at location 2 :
4
Enter number at location 3 :
1
Enter number at location 4 :
5
{1, 2, 4, 5}
'''
