import numpy as np

#here we have an array of 4 students grades for 3 exams
#row = each student (stu0, stu1, stu2, stu3)
#column = each test (test0, test1, test2)

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])


#indexing and slicing

student1 = grades[1]

student0_test1 = grades[0,1]

students0_1 = grades[0:2]   #upper limit not included in this #colon for sequential rows

students1and3 = grades[[1,3]]      #double bracket because we only specify rows

students1and3_test2 = grades[[1,3], 2]

all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]

all_student_test0and2 = grades[:,[0,2]] #non sequential order of the tests (test 0 and 2 for all students)


import random
grades = np.random.randint(60,101,12).reshape(3,4)



average = grades.mean()

#by column
all_test = grades.mean(axis=0)

#by row
each_student = grades.mean(axis=1)



#shallow and deep copies
#shallow aything changed in original array changes the view
#deep copy

numbers = np.arange(1,6)

numbers_view = numbers.view()   #creates view of original array

numbers[1] *= 10    #both have changed because we see whats in the original array

numbers_view[1] /= 10       #change view it affects original array and vice versa with shallow copy

#slice creates shallow copy

numbers_slice_view = numbers[0:3]

numbers[1] *= 20


#deep copy

numbers_copy = numbers.copy()       #creates copy without affecting original array

numbers[1] *= 10

#reshape crates shallow copy of original array

grades = np.array([[87,96,70],[100,87,90]])

grades_reshaped = grades.reshape(1,6)

#grades.resize(1,6)  #this modifies the original array (not deep copy)

flattended = grades.flatten()   #creates deep copy of original array

#ravel method produces a shallow copy
raveled = grades.ravel()

raveled[0] = 100

raveled[5] = 99



print()


