## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

array = salesArray.sum()
print('Total sales: ',array)

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

small = np.min(salesArray)
large = np.max(salesArray)
print('Smallest sale: ',small)
print('Largest sale: ',large)


## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")

print('Sales greater than 100: ', salesArray[salesArray >= 100])


## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

Each_register = np.sum(salesArray, axis = 1)
for x in range(len(Each_register)):
    print('Reg', x + 1, 'Sale: ', Each_register[x])


## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")

credit_card = []
for x in range(len(salesArray)):
    k = []
    for c in range(len(salesArray[0])):
        l = .02 * salesArray[x][c]
        l = (round(l, 2))
        k.append(l)
    credit_card.append(k)

fee_total = sum(map(sum,credit_card))
for x in credit_card:
    print(x)

print('Fee total: ', round(fee_total, 2))



## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

profit_array = []
for x in range(len(credit_card)):
    h = []
    for c in range(len(credit_card[0])):
        b = salesArray[x][c] - credit_card[x][c]
        b = round(b, 2)
        h.append(b)
    profit_array.append(h)

profit_total = sum(map(sum,profit_array))
for x in profit_array:
    print(x)

print('Profit total:', profit_total)


## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")

for x in range(1,len(salesArray), 2):
    print(salesArray[x])






## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([[17.89,13.59,107.89,176.88,56.78]])

salesArray = np.concatenate((salesArray, newRegister), axis = 0)

for x in salesArray:
    print(x)





## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")

print('Before modification: ')
for x in salesArray:
    print(x)

salesArray[2][3] = 20.14

print('After modification: ')
for x in salesArray:
    print(x)





#done