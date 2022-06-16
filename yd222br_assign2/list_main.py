import list_functions as lf

A = lf.random_list(5)
print(A)

B = lf.average([1,2,3,4,5,6,7,8])
print(B)

C = lf.only_odd([1,2,3,4,5,6,7,8])
print(C)

lf.to_string([1,2,3,4,5,6,7,8,9])

D = lf.contains([1,2,3,4],2,3)
print(D)

E = lf.contains([1,2,3,4],2,4)
print(E)

F = lf.has_duplicates([1,2,3,4,5,6,7])
print(F)

G = lf.has_duplicates([1,2,3,3,4,5,6])
print(G)
