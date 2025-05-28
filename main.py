
def find_coins_greedy(amount:int, available_coins:list):
    available_coins.sort(reverse=True)
    change= {}
    for coin in available_coins:
        num_of_coins = amount//coin
        if num_of_coins:
            amount -= num_of_coins * coin
            change[coin] = num_of_coins
        if amount < available_coins[-1]: break

    return change, amount

def find_min_coins(amount:int, available_coins:list):
    K = [float('inf') for _ in range(amount + 1)]
    K[0] = 0
    change = [[0 for _ in available_coins] for _ in K]

    for c_ind, coin in enumerate(available_coins):
        for i in range(coin, amount + 1):
            if K[i-coin] + 1 < K[i]:
                K[i] = K[i-coin] + 1
                change[i] = change[i - coin].copy()
                change[i][c_ind] += 1

    # print(K)
    # for i, x in enumerate(change):
    #     print(f'{i} - {x}')

    if K[amount] == float('inf'):
        return {}, amount
    return {available_coins[i]:change[amount][i] for i in range(len(available_coins))if change[amount][i]>0}, 0

coins= [50, 10, 5, 2, 1, 25]
amount = 113

dict, extra_sum = find_coins_greedy(amount, coins)
if extra_sum:
    print(f'Available coins do not cover the need! The balance is {extra_sum}')
else:
    print('Your change with greedy algorithm:')
    for coin, num in dict.items():
        print(f'{coin:3} : {num:3} шт.')

dict, extra_sum = find_min_coins(amount, coins)
if extra_sum:
    print(f'Available coins do not cover the need! The balance is {extra_sum}')
else:
    print('Your change with dynamic programing:')
    for coin, num in dict.items():
        print(f'{coin:3} : {num:3} шт.')