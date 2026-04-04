from itertools import combinations

NOT_POSSIBLE = [None] * 200

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    return dynamic_programming(coins, target)

def dynamic_programming(coins, target):
    change_mapping = {0: []}
    for total_value in range(1, target + 1):
        usable_coins = [coin for coin in coins if coin <= total_value]
        coin_combos = [change_mapping[total_value - coin_value] for coin_value in usable_coins]

        if not coin_combos:
            change_mapping[total_value] = NOT_POSSIBLE
        else:
            best_combo = coin_combos[0]
            for combo in coin_combos[1:]:
                if len(combo) < len(best_combo):
                    best_combo = combo

            if best_combo == []:
                change_mapping[total_value] = [total_value]
            elif best_combo == NOT_POSSIBLE:
                change_mapping[total_value] = NOT_POSSIBLE
            else:
                change_mapping[total_value] = best_combo + [total_value - sum(best_combo)]

    if change_mapping[target] == NOT_POSSIBLE:
        raise ValueError("can't make target with given coins")

    return sorted(change_mapping[target])

def brute_force(coins, target):
    max_per_coin = {}
    for coin_value in coins:
        max_per_coin[coin_value] = target // coin_value

    coin_options = []
    for coin_value, num_coins in max_per_coin.items():
        coin_options += [coin_value] * num_coins

    max_coins = max(max_per_coin.values())
    min_coins = min(max_per_coin.values())
    for num_coins in range(min_coins, max_coins + 1):
        for coin_combo in combinations(coin_options, num_coins):
            if sum(coin_combo) == target:
                return list(coin_combo)

    raise ValueError("can't make target with given coins")




def greedy_algorithm(coins, target):
    change = []
    coins_decending = sorted(coins, reverse=True)
    remaining = target

    for coin_value in coins_decending:
        if remaining >= coin_value:
            num_coins = remaining // coin_value
            change += [coin_value] * num_coins
            remaining = remaining % coin_value

    if sum(change) == target:
        return list(reversed(change))
    
    return brute_force(coins, target)
