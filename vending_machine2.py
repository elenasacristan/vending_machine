'''
We import the byotest framework the asterisc "*" is for importing everything
'''
from byotest import *

coins_euros = {100:20 ,50:20, 20:20, 10:20, 5:20, 2:20, 1:20}
usd_coins = {100:20, 50:20, 25:20, 10:20, 5:20, 1:20}


def change(amount, coins=coins_euros):
    # if amount==0:
    #   return []
    # if amount in coins_euros:
    #     return [amount]
    
    # if amount==0:
    #     return []
    
    change = []
    for coin in sorted(coins.keys(), reverse=True):
        while coin <= amount and coins[coin] > 0:
            amount -= coin
            coins[coin] -= 1
            change.append(coin)
    
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
        
    return change
    
    
            
    # for key, value in coins.items():
        
    #     while amount >= key:
    #         amount = amount-key
    #         change.append(key)
    # return change
        
    
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
test_are_equal(change(5, {2:1,1:4}),[2,1,1,1])
test_are_equal(change(10, {2:2,1:10}),[2,2,1,1,1,1,1,1])
test_exception_was_raised(change, (5, {2: 1, 1: 2}),
    "Insufficient coins to give change.")










print("All test pass")