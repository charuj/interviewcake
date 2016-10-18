'''
2. You have a list of integers, and for each index you want to find the product of every
integer except the integer at that index.

'''

import numpy as np

def get_products_of_all_ints_except_at_index(list):

    product_list=[]
    if len(list)==1:
        return None

    for i in range(len(list)):
        product_list.append(np.product(list[:i])*np.product(list[i+1:]))


    return product_list



#TEST CASES

t1=[4]   # only one index/number in the list
t2=[4,5]  # only two numbers in the list
t3= [1,2,3,4,5]  # only positive numbers
t4= [-1,-2,-3,-4]  # only negative numbers
t5= [-10, 1,2,4,-2]  # positive and negative numbers
test=[t1, t2, t3,t4,t5]

# Answers
t1a= None
t2a= [5,4]
t3a= [120, 60, 40, 30,24]
t4a=[-24, -12,-8,-6]
t5a=[-16, 160, 80,40,-80 ]
answers= [t1a, t2a,t3a,t4a,t5a]

for i in range(len(test)):
    product= get_products_of_all_ints_except_at_index(test[i])
    if product != answers[i]:
        print "Case " + str(i+1) + " expected " + str(answers[i]) + " but got: " + str(product)
    else:
        print "Case " + str(i+1) + " works!" + "got: " + str(product)
