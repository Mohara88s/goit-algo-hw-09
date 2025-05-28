import timeit
from algorithms import find_coins_greedy, find_min_coins


def time_analyzing_func(amount, coins, func, func_name):
    start_time = timeit.default_timer()
    func(amount, coins)
    end_time = timeit.default_timer()
    duration = end_time - start_time
    print(f'    - {func_name} duration - {duration}s.')
    return duration


def main():
    coins = [50, 10, 5, 2, 1, 25]
    amounts = [113, 1137, 11379, 113797, 1137979]

    for amount in amounts:
        print(f'\nTest for amount - {amount}')
        find_coins_greedy_duration = time_analyzing_func(amount, coins, find_coins_greedy, 'find_coins_greedy')
        find_min_coins_duration = time_analyzing_func(amount, coins, find_min_coins, 'find_min_coins')
        print(f'The dynamic programming function is {find_min_coins_duration/find_coins_greedy_duration} times slower than the greedy algorithm function in the current test')


if __name__ == "__main__":
    main()
