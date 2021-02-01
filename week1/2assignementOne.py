import numpy as np

# Exercise - Array Creation
# array 1
arrayOne = np.ones((4, 4))
arrayOne[2, 3] = 2
arrayOne[3 , 1] = 6

# array 2
arrayTwo = np.zeros((1, 5))
arrayTwo = np.append(arrayTwo, np.diag(np.arange(2, 7)),axis=0) # appending 


# Exercise - Tiling for array creation
arrayThree = np.array([[4, 3], [2, 1]])
arrayThree = np.tile(arrayThree, (2, 3))    # repeat 2 times the rows, and 3 times the columns


print("\n<- Array Creation ->\n\t____first____\n" + str(arrayOne))
print("\t___second___\n" + str(arrayTwo))
print("\n\n<- Tiling for array creation ->\n"+str(arrayThree))