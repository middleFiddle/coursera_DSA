def change(money):
    coins = 0
    while money > 0:
        if money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        else:
            money = money - 1 
        coins = coins + 1
    return coins
        
if __name__ == '__main__':
    m = int(input())
    print(change(m))
