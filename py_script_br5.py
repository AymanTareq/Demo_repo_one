print("I will merge branch4 and branch5 with main branch")
print("As a result, features developed in branch4 and branch5 will be available in main branch")
print("It's cool. :)")

## Let's see another way to remvoe duplicate from a list

lst1 = ['a','b','c','d','d','c','d','b']

print("Before removing duplicate:",lst1)

lst1 = list(set(lst1))
lst1.sort()

print("After removing duplicate:",lst1)
