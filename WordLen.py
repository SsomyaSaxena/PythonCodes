a=[]
n=int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item =(input())
    a.append(item)

def match(w):
 ctr = 0

 for word in w:
   if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
 return ctr

print("output:",match(a))


#OUTPUT:
'''
Enter the list size : 4
Enter number at location 0 :
abc
Enter number at location 1 :
xyz
Enter number at location 2 :
aba
Enter number at location 3 :
1221
output: 2
'''
