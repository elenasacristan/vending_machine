'''
We import the byotest framework the asterisc "*" is for importing everything
'''
from byotest import *

coins_euros = [100,50,20,10,5,2,1]
usd_coins = [100,50,25,10,5,1]


def change(amount, coins=coins_euros):
    # if amount==0:
    #   return []
    # if amount in coins_euros:
    #     return [amount]
    
    change = []
    
    for coin in coins:
        while amount >= coin:
            amount = amount-coin
            change.append(coin)
    return change
        
    
test_are_equal(change(0),[])
test_are_equal(change(1),[1])
test_are_equal(change(2),[2])
test_are_equal(change(5),[5])
test_are_equal(change(10),[10])
test_are_equal(change(20),[20])
test_are_equal(change(50),[50])
test_are_equal(change(100),[100])
test_are_equal(change(3),[2,1])
test_are_equal(change(7),[5,2])
test_are_equal(change(9),[5,2,2])
test_are_equal(change(35, usd_coins),[25,10])









print("All test pass")