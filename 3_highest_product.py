'''

3.Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.

'''
import heapq
import numpy as np

def highest_product(list_of_ints):

    # if all positive or negative numbers
    prod=0
    if all(x<0 for x in list_of_ints) or all(x>0 for x in list_of_ints):
        largest= heapq.nlargest(3,list_of_ints)
        prod= np.product(largest)
        return prod
    else: # if the list contains both positive and negative numbers
        max_positive_product= list_of_ints[-1] * list_of_ints[-2] * list_of_ints[-3]
        list_of_ints.sort()
        # the only solution containing negative numbers will have 2 neg numbers
        if list_of_ints[0]<0 and list_of_ints[1]<0:
            temp_product = list_of_ints[0]*list_of_ints[1]*list_of_ints[-1]
            if temp_product > max_positive_product:
                return temp_product



#TEST CASES

t1= [2,2,2,2] # more than three integers, all the same
t2= [2,5,8,3] # list of all positive integers
t3= [-5,-76,-3,-1] # list of all negative integers
t4= [-6, 7, 8,-50] # list of positive and negative integers, largest ints wont give max product

test=[t1,t2,t3,t4]

#Answers
t1a= 8
t2a= 120
t3a= -15
t4a= 2400
answers=[t1a, t2a, t3a, t4a]


for i in range(len(test)):
    prod= highest_product(test[i])
    if prod != answers[i]:
        print "Case " + str(i+1) + " expected " + str(answers[i]) + " but got: " + str(prod)
    else:
        print "Case " + str(i+1) + "works!"