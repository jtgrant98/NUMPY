import numpy as np
import random 

arr01 = np.array([[1,2,3],[4,5,6]])

#2 rows and 3 columns
#2 dimensional array
#each set represent a row and within each bracket represents a column

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

'''
for row in arr01:
    print(row)
    input()
    for column in row:
        print(column,end = ' ')
    print()

for i in arr01.flat:
    print(i)
'''

arr03 = np.zeros(5)

arr04 = np.ones((2,4),dtype=int)

arr05 = np.full((3,5),13)


print()

#create 2 dimensinal array of 5 integer elements each using random moduel
#and list comprehension point out its dimension, shape and size

a = np.array([[random.randint(1,10) for i in range (5)],[random.randint(1,10) for i in range (5)]])

b = np.array(np.random.randint(1,10,size=(2,5)))

arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange (10,1,-2)

arr09 = np.linspace(0.0,1.0,num = 5)

arr10 = np.arange(1,21).reshape(4,5)    #make sure the specification is the right size 


num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3

num01 += 10 #this changes original array

num04 = num01 * num02 #will only work if these arrays have the same size and shape

num05 = num01 > 13

num06 = num03 > num01

#here we have an array of 4 students grades for 3 exams
#row = student
#column = exam

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())


#specifically by rows or columns we can do that too

grades_by_exam = grades.mean(axis=0)        #all row values in each column

#axis = 0 means we are going by column (calculated average for every row by column)

grades_by_student = grades.mean(axis=1)

#axis = 1 means we take all grades by row and average them 

num07 = np.array([1,4,9,16,25,36])

num08 = np.sqrt(num07)

num09 = np.array([10,20,30,40,50,60])

num10 = np.add(num07,num09)     #have to be same size to add them together 

num11 = np.multiply(num09,5)    #This is BROADCASTING because 5 is applied to each element 

num12 = num09.reshape(2,3)      #2 rows with 3 columns

num13 = np.array([2,4,6])

num14 = np.multiply(num12,num13)        #you can have as many rows as you want but the columns have to be specific




print()