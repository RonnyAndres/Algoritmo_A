


import copy


A = [2,3,1,4]
B = [4,1,3,2]

print(sorted(A))
# ordenar la lista B en orden descendente
b = copy.deepcopy(B)
b.sort(reverse=True)
print(b)
