import pytest
from inventory_simulation import simulate_inventory


def test_extreme_inventory():
    # 極端に少ない・多い在庫のとき、コストが大きくなるはず
    low_stock = simulate_inventory(10, trials=5000)
    high_stock = simulate_inventory(150, trials=5000)
    middle_stock = simulate_inventory(60, trials=5000)
    print(f"low: {low_stock}, middle: {middle_stock}, high: {high_stock}")
    assert middle_stock < low_stock
    assert middle_stock < high_stock

def test_reasonable_output_type():
    # 戻り値が float であること
    cost = simulate_inventory(50, trials=1000)
    assert isinstance(cost, float)
    
def test_cost_curve_has_minimum():
    stock_range = range(30, 100, 10)
    results = [(stock, simulate_inventory(stock, trials=5000)) for stock in stock_range]
    stocks, costs = zip(*results)

    print("\n--- 在庫数 vs コスト ---")
    for stock, cost in results:
        print(f"在庫数: {stock} -> コスト: {cost:.2f}")

    min_cost = min(costs)
    min_index = costs.index(min_cost)

    # 最小コストが真ん中付近にある
    assert 1 < min_index < len(costs) - 2


