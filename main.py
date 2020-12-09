##
##
##
##
can_be_crafted = ["Claymore", "Broadsword", "Dualsword"]
while True:
    to_be_crafted = {input("To be crafted:").title()}
    if to_be_crafted.issubset(can_be_crafted):
        break
    else:
        print("Please enter a sword type.")
##
while True:
    amount_crafted = input("How many to be crafted:")
    val = int(amount_crafted)
    if val > 0:
        break
    else:
        print("Please enter a number.")

while True:
    sword_crafting_lvl = input("Sword Crafting Level:")
    val = int(sword_crafting_lvl)
    if val > 0:
        break
    else:
        print("Please enter a number")
while True:
    tbc_lvl = input(f"{to_be_crafted} Crafting Level: ")
    val = int(tbc_lvl)
    if val > 0:
        break
    else:
        print("Please enter a number")
##
if to_be_crafted == "Claymore":
    from claymore1 import (focus_cost_calc)
    focus_cost_calc()
##
new_cost = focus_cost_calc()
##
while True:
    metal_bar = input("Metal Bar:")
    val = int(metal_bar)
    if val > 0:
        break
    else:
        print("Please enter a number greater than zero")

while True:
    leather = input("Leather:")
    val = int(leather)
    if val > 0:
        break
    else:
        print("Please enter a number greater than zero")


while True:
    price_of_sword = input(f"{to_be_crafted}Selling Price:")
    val = int(price_of_sword)
    if val >= 0:
        break
    else:
        print("Please enter a number\n"
              "If unknown enter 0: ")

val1 = float(metal_bar)
val2 = float(leather)
cost_to_craft = (val1 * 20 + val2 * 12) * 0.54

if price_of_sword == 0:
    val1 = int(cost_to_craft)
    val2 = int(amount_crafted)
    print(f"Sell above: {val1} Silver")
    print(f"Total Profit{val1 * val2}")
    print(f"Total Focus: {new_cost * val2} Focus")
else:
    if cost_to_craft < int(price_of_sword):
        profit = int(price_of_sword) - cost_to_craft
        print(f"Total Profit: {profit * val2} Silver")
        print(f"Total Focus: {new_cost * amount_crafted} Focus")
    else:
        print("Not profitable")
