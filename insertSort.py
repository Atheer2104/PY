def insert(array):
    for index in range(1,len(array)):

     currentvalue = array[index]
     position = index

     while position > 0 and array[position-1]>currentvalue:
         array[position] = array[position-1]
         position = position-1

     array[position]=currentvalue



array = [22, 11, 99, 88, 9, 7, 42]
insert(array)
print(array)

