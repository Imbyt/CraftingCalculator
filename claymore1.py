focus_cost = {

    "4.0": 1000, "4.1": 1000, "4.2": 1000, "4.3": 1000,
    "5.0": 1000, "5,1": 1000, "5.2": 1000, "5.3": 1000,
    "6.0": 1000, "6,1": 1000, "6.2": 1000, "6.3": 1000,
    "7.0": 1000, "7,1": 1000, "7.2": 1000, "7.3": 1000,
    "8.0": 1000, "8,1": 1000, "8.2": 1000, "8.3": 1000,
}


def focus_cost_calc():
    claymore_lvl = int(input("Claymore Crafting level: "))
    sword_crafting_lvl = int(input("Sword Crafting level: "))
    what_tier = input("What tier ex. 5.3 : ")

    tier = int(focus_cost[what_tier])

    focus_cost_efficiency = 280 * claymore_lvl + sword_crafting_lvl * 30
    new_focus = int(tier * 0.5 ** (focus_cost_efficiency / 10000))





