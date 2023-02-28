s1 ={"AB",2,3,4,2001,34,"Haripur"}

s2 ={"Mohiz",2,3,4,2001,2002,34,"Abbottabad"}

#update and union
# s1.update(s2)
# print(s1)
print(s1.union(s2))

s4 = {5, 2, 7, 3}

#Printing an empty set
s3 = set ({})
print(type(s3))

#intersection and update of sets
#s1 is updated thats why different output
print(s1)
print(s2)
s5 = s1.intersection(s2)
print(s5)


#Symmetric difference
#Values that are not common in set
symmetric = s1.symmetric_difference(s2)

print(symmetric)

# More methods
# disjoint Sets
s6 = s1.isdisjoint(s2)
print(s6)

# superset
# checks if all item of a particular set are present in the original set.

s7 = s1.issuperset(s2)
print(s7)

# SUBSET
# checks if all item of a original set are present in the particular  set.

s8 = s1.issubset(s2)
print(s8)

# REMOVE AN ITEM FROM SET
print(s2)
s2.remove("Mohiz")
print(s2)

#DELETE ENTIRE SET
print(s2)
del s2
print("NOW THE SET 2 is removed you cannot acces after that")
 #NOW THE SET 2 is removed
