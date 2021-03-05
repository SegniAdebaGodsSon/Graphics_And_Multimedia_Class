import numpy as np 

a = np.array([[0, 1, 2], [3,4,5]])
list = [1,2,3,4]
b=np.array(list)
c=np.arange(10)
d=np.arange(1,9,2)
e=np.ones((3,3))    
f=np.zeros((2,2))
g=np.eye(3)
h=np.diag(np.array([1,2,3,4]))
i=np.diag(np.arange(3))

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)


# print(a[0,1])
# print(a[0])

# print(c[0:9:4])
# print(c[2:])
# print(c[:6])
# print(c[::2])

# print(a.size)
# print(a.dimension)
# print(a.shape)




td = np.diag(np.arange(1,5))

# for i in range(4):
#     print(td[i,i])


# print(td[0])



arr = []
for i in range(6):
    ar = []
    for j in range(i*10, i*10+6):
        ar.append(j)
    arr.append(ar)
arr = np.array(arr)
# print(arr)

# print(arr[0, 3:5])
# print(arr[4:, 4:])
# print(arr[:, 2])
# print(arr[2::2, ::2]) # ???


# fancy indexing operations returns 1 dimensional arrays
# boolean
# print(arr[arr%2==0])    # get even elements
# arr[arr%2==0] = -1
# print(arr)

# manipulate
# arr2 = np.arange(10)
# print(arr2)
# arr2[::2] += 10
# print(arr2)

# print(arr2[[2, 3, 4]])

# arr2[[0,1]] = 777
# print(arr2)



arr3 = [[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr3 = np.array(arr3)

# print(arr3.min())
# print(arr3.max())
