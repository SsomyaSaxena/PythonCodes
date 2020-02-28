def l(n):
    return n[-1]

def sort(tuples):
  return sorted(tuples, key=l)

print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


#OUTPUT:
'''
[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
