print("Enter prices of 6 items:")
prices = []
for i in range(1, 7):
    price = float(input(f"Item {i}: "))
    prices.append(price)
print()
budget = float(input("Enter total budget: "))
print()
current_total = 0
bought_items = []
for i in range(6):
    item_num = i + 1
    price = prices[i]
    p_disp = int(price) if price.is_integer() else price
    if current_total + price <= budget:
        status = "buy"
        current_total += price
        bought_items.append(p_disp)
    else:
        status = "cannot buy"
    c_disp = int(current_total) if current_total.is_integer() else current_total
    print(f"Item {item_num} = {p_disp} -> {status}")
    print(f"Current total = {c_disp}\n")
remaining_budget = budget - current_total
b_disp = int(budget) if budget.is_integer() else budget
rem_disp = int(remaining_budget) if remaining_budget.is_integer() else remaining_budget
print("--- Summary ---")
print(f"Bought items: {bought_items}")
print(f"Total spent: {c_disp}")
print(f"Remaining budget: {rem_disp}")