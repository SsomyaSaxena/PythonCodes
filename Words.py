string=input("Enter your String!")
x=int(input("Enter the length you want:"))
def words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(words(x,string))


#OUTPUT:
'''
Enter your String! HELLO SSOMYA
Enter the length you want: 5
['SSOMYA']
'''

