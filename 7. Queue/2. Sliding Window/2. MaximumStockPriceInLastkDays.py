"""
You have to find the maximum stock price withing the last k days. Say u have been given an array -
[ (1, 2), (4, 4), (3, 7), (2, 9), (5,11) ] where the first elem denotes the stock price and the next elem denotes the day,
Then the to find the stock price in the last k days or say last 4 days - u will have to create a queue that stores the max price
the last 4 days... Our final queue will have the stock prices for the last 4 days only.. say u have been given
data till index 1.. then queue will have stocks (1,2) and (4,4) so max price will be 4..

"""
import sys

q = []


class Stock:

    def __init__(self, price, day):
        self.price = price
        self.day = day

class StockPrice:

    def __init__(self, n = 3):
        self.q = []
        self.window = n

    def addStock(self, price, day):

        # Check if the new stock u are going to add, if it has more difference than the stock at end the queue, we pop
        # Check this condition -

        while self.q and self.q[0].day < (day - self.window + 1):
            self.q.pop(0)

            print('After pop - ')
            self.printQueue()
        self.q.append(Stock(price, day))
        print('After final add - ')
        self.printQueue()

    def getMax(self):

        maxElem = -sys.maxsize
        for i in self.q:
            price = i.price
            maxElem = max(maxElem, price)

        return maxElem

    def printQueue(self):

        for i in self.q:
            print(i.price, i.day)

s = StockPrice(4)

s.addStock(1, 2)
s.addStock(4, 4)
print('Max yet - ',s.getMax())
s.addStock(3, 7)
print('Max yet - ',s.getMax())
s.addStock(2, 9)
print('Max yet - ',s.getMax())
s.addStock(5, 11)
print('Max yet - ',s.getMax())



