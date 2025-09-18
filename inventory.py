# inventory.py

from math import sqrt

def calculate_eoq(demand, ordering_cost, holding_cost):
    """Calculate Economic Order Quantity (EOQ)."""
    return sqrt((2 * demand * ordering_cost) / holding_cost)


def calculate_rop(daily_demand, lead_time_days, safety_stock=0):
    """Calculate Reorder Point (ROP)."""
    return (daily_demand * lead_time_days) + safety_stock


def calculate_safety_stock(max_daily_demand, avg_daily_demand, lead_time_days):
    """Calculate Safety Stock."""
    return (max_daily_demand - avg_daily_demand) * lead_time_days


def calculate_total_cost(demand, ordering_cost, holding_cost, eoq):
    """Calculate Total Inventory Cost."""
    return (demand / eoq) * ordering_cost + (eoq / 2) * holding_cost


def calculate_bulk_discount_eoq(demand, ordering_cost, holding_cost_rate, price_breaks):
    """
    Calculate EOQ considering bulk discounts.
    price_breaks: list of tuples (min_qty, unit_price)
    Returns dictionary with best order quantity, unit price, and total cost.
    """
    price_breaks.sort(key=lambda x: x[0])  # Sort by min quantity

    best_order_qty = 0
    best_unit_price = 0
    min_total_cost = float('inf')

    for min_qty, unit_price in price_breaks:
        holding_cost = unit_price * holding_cost_rate
        eoq = sqrt((2 * demand * ordering_cost) / holding_cost)

        # If EOQ < min_qty, order at min_qty
        order_qty = max(eoq, min_qty)

        total_cost = (order_qty / 2 * holding_cost) + (demand / order_qty * ordering_cost) + (demand * unit_price)

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_order_qty = order_qty
            best_unit_price = unit_price

    return {
        "order_qty": best_order_qty,
        "unit_price": best_unit_price,
        "total_cost": min_total_cost
    }
