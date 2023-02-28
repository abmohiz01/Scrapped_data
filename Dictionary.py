thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dct1 = {1 : 11, 2 :22, 3 : 33, 4 : 44,5:55}
print(dct1)
print(thisdict)
for key in dct1.keys():
  print(dct1[key])

print(dct1.values())

# METHODS IN DICTIONARY

#UPDATE DICTIONARY

thisdict.update(dct1)
print(thisdict)

# POP
# Removes a key in Parameter

thisdict.pop("brand")
print(thisdict)

#POP ITEM METHOD
dct1.popitem()
print(dct1)

