import numpy as np

elements = [1, 2, 8, 0, 0, 0, 0] #this is a type list
elementsArray = np.array(elements, int) #this is a type numpy,ndarray
vectorSize = len(elementsArray) #len() takes the size of the array in an int
vectorShape = np.shape(elementsArray) #.shape takes the size of an array ina tuple (value,)

totalElementsSum = 0
for element in elementsArray:
    totalElementsSum += element
print('soma total dos valores do array: ', totalElementsSum)

print('agora as triplas: ')

if (vectorSize >= 3):
    for element in elementsArray:
        pass

print(np.arange(3, 25, 1, int))
