from sys import argv


def sulary(l_hours, price, profit):
    result = (l_hours * price) + (l_hours * price) * profit
    return result


script, l_hous, price, profit = argv
sulary(l_hours, price, profit)