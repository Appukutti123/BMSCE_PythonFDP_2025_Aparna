# list is mutable, ordered collection of data

# properties
# ordered
# Mutable
# Allows Duplicates

# In other languages we have arrays ----> int arr[]

a = [1, "Hello", 10.5, True]

myList = [1,2,3,4,5,6,7,8,9,10]
anotherList = list(range(2,101,2))

# 1) Accessing the Elements

print(myList)
print(anotherList)
print(myList[2])
print(myList[2:3]) # TAKING sLICE OUT OF THE MAIN LIST
print(myList[-8:-3])

# 2) Modifying the list

myList[-2] = 300
myList.append(11)
print(myList)
myList.insert(5, 3000)
myList.insert(6, 5000)
print(myList)
myList.pop()
print(myList)

# 3) Other Functions
print(len(myList))
myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)



