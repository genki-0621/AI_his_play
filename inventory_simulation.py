# inventory_simulation.py

import numpy as np

intervals = [(26, 37), (37, 48), (48, 60), (60, 100)]
weights = [0.2, 0.3, 0.3, 0.2]

def simulate_inventory(stock: int, trials: int = 10000, shortage_cost=2, overstock_cost=1):
    shortage = 0
    overstock = 0
    for _ in range(trials):
        interval = intervals[np.random.choice(len(intervals), p=weights)]
        demand = np.random.uniform(*interval)
        if stock < demand:
            shortage += demand - stock
        else:
            overstock += stock - demand
    total_cost = shortage * shortage_cost + overstock * overstock_cost
    return round(total_cost, 2)

