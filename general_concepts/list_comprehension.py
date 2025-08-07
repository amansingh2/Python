arr = [x for x in range(0 , 5)]

print(arr)


square_arr = [x**2 for x in range(0 , 5) if x % 2 == 0]
print(square_arr)

arr1 = [1 , 2]

arr1.append(5)
print(arr1[2])

arr2 = []
arr2.append([1 , 2 , 2])
arr2.append([1 , 2 , 2])
arr2.append([1 , 2 , 2])
print(arr2[1])
