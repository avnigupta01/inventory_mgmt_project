from inventory import calculate_eoq, calculate_reorder_point, calculate_bulk_discount, calculate_safety_stock, calculate_total_cost

def run_tests():
    print("=== Testing Inventory Library Functions ===")
    
    eoq = calculate_eoq(1000, 50, 2)
    print(f"EOQ (Expected ~223.61): {eoq:.2f}")
    
    reorder_point = calculate_reorder_point(40, 5)
    print(f"Reorder Point (Expected 200): {reorder_point}")
    
    bulk_discount = calculate_bulk_discount(1000, 50, 2, [(0, 20), (100, 18), (500, 15)])
    print(f"Bulk Discount Total Cost (Example Output): {bulk_discount:.2f}")
    
    safety_stock = calculate_safety_stock(50, 10, 2)
    print(f"Safety Stock (Expected 100): {safety_stock}")
    
    total_cost = calculate_total_cost(1000, 50, 2, 20)
    print(f"Total Cost (Example Output): {total_cost:.2f}")

if __name__ == "__main__":
    run_tests()
