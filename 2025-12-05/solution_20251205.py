f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-05\\input.txt")

def Check_Freshness(fresh_range,ingredient):
    range_start,range_finish = fresh_range.split("-")
    range_start = int(range_start)
    range_finish = int(range_finish)
    ingredient = int(ingredient)
    if ingredient >= range_start and ingredient <= range_finish: return True
    return False

def main(fresh_ranges,ingredients):
    fresh_ingredients = []
    for range in fresh_ranges:
        for ingredient in ingredients:
            if ingredient in fresh_ingredients: continue
            if (Check_Freshness(range,ingredient)): fresh_ingredients.append(ingredient)
    print(len(fresh_ingredients))


arr = []
for line in f:
    if line.strip() == "":
        fresh_ranges = arr
        arr = []
        continue
    arr.append(line.strip())
ingredients = arr

main(fresh_ranges,ingredients)
