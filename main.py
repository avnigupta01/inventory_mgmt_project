# main.py
from inventory import (
    calculate_eoq,
    calculate_rop,
    calculate_safety_stock,
    calculate_total_cost,
    calculate_bulk_discount_eoq
)

def get_float(prompt):
    """Helper function to safely get float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def main():
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Calculate EOQ")
        print("2. Calculate Reorder Point (ROP)")
        print("3. Calculate Safety Stock")
        print("4. Calculate Total Cost")
        print("5. Calculate EOQ with Bulk Discount")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            D = get_float("Enter annual demand (units/year): ")
            S = get_float("Enter ordering cost per order: ")
            H = get_float("Enter holding cost per unit: ")
            eoq = calculate_eoq(D, S, H)
            print(f"EOQ = {eoq:.2f} units")

        elif choice == "2":
            daily_demand = get_float("Enter daily demand: ")
            lead_time = get_float("Enter lead time (days): ")
            safety_stock = get_float("Enter safety stock (optional, 0 if none): ") or 0
            rop = calculate_rop(daily_demand, lead_time, safety_stock)
            print(f"Reorder Point (ROP) = {rop:.2f} units")

        elif choice == "3":
            max_demand = get_float("Enter maximum daily demand: ")
            avg_demand = get_float("Enter average daily demand: ")
            lead_time = get_float("Enter lead time (days): ")
            safety_stock = calculate_safety_stock(max_demand, avg_demand, lead_time)
            print(f"Safety Stock = {safety_stock:.2f} units")

        elif choice == "4":
            D = get_float("Enter annual demand (units/year): ")
            S = get_float("Enter ordering cost per order: ")
            H = get_float("Enter holding cost per unit: ")
            eoq = calculate_eoq(D, S, H)
            total_cost = calculate_total_cost(D, S, H, eoq)
            print(f"Total Inventory Cost = {total_cost:.2f}")

        elif choice == "5":
            try:
                D = get_float("Enter annual demand (units/year): ")
                S = get_float("Enter ordering cost per order: ")
                holding_rate = get_float("Enter holding cost rate (as % of unit cost, e.g., 5 for 5%): ") / 100

                n = int(get_float("Enter number of price breaks: "))
                price_breaks = []
                for i in range(n):
                    min_qty = get_float(f"Enter min quantity for price break {i+1}: ")
                    unit_price = get_float(f"Enter unit price at this level: ")
                    price_breaks.append((min_qty, unit_price))

                result = calculate_bulk_discount_eoq(D, S, holding_rate, price_breaks)
                print(f"\nBest Order Quantity = {result['order_qty']:.2f} units")
                print(f"Unit Price = {result['unit_price']}")
                print(f"Total Cost = {result['total_cost']:.2f}")

            except ValueError:
                print("Invalid input! Please enter valid numeric values.")

        elif choice == "6":
            confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower()
            if confirm == 'y':
                print("Exiting system...")
                break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
