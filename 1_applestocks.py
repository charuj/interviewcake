'''

https://www.interviewcake.com/question/python/stock-price

1. Write an efficient function that takes stock_prices_yesterday and returns the best profit I
could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

'''


def get_max_profit(stock_prices_yesterday):
    return



## Test cases
t1=[5,5,5,5,5,5]   # price is the same at every minute of the day (i.e. profit = 0)
t2=[100,90,80,40,10,5]   # Only losses (negative profit). Ever price is lower than the preceding prices. Return minimum loss
t3=[10, 7, 5, 8, 11, 9]   # One max profit.Buying for 5, selling for 11, returns 6
t4=[10,16, 5,8,11,9]   # multiple of the same maximum profits; two cases of 6
t5=[]   # Empty price list (error)
test= [t1, t2, t3,t4,t5]

# answers
t1a= 0
t2a= -5 # returns the smallest loss
t3a= 6
t4a= 6
t5a= None
answers= [t1a, t2a, t3a, t4a, t5a]


for i in range(len(test)):
    profit= get_max_profit(test[i])
    if profit != answers[i]:
        print "For case " + str(i+1) + " expected " + str(answers[i]) + " but got " + str(profit)
    else:
        print "Case " + str(i+1) + " works!"