f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-05\\input_sample2.txt")

def Check_Freshness(fresh_range,ingredient):
    range_start,range_finish = fresh_range.split("-")
    range_start = int(range_start)
    range_finish = int(range_finish)
    ingredient = int(ingredient)
    if ingredient >= range_start and ingredient <= range_finish: return True
    return False

def Check_Indvidual_Range(r,fresh_ranges):
    rs,rf = r.split("-")
    rs = int(rs)
    rf = int(rf)
    for r2 in fresh_ranges:
        print(r+" <>" + r2)
        if r == r2: 
            print("continue")
            continue
        elif (Check_Freshness(r2,rs) and Check_Freshness(r2,rf)):
            return False
        elif Check_Freshness(r2,rs):
            print("start is removed")
            #if start falls into any range
            rs = r2.split("-")[0]
        elif Check_Freshness(r2,rf):
            print("end is removed")
            #if end falls into any range
            rf = r2.split("-")[1]
    new_r = str(rs)+"-"+str(rf)
    print(new_r+" is added")
    return new_r


def main(fresh_ranges):
    new_range = []
    for r in fresh_ranges:
        new_r = Check_Indvidual_Range(r,fresh_ranges)
        if new_r == False:
            continue
        if new_r not in new_range: 
            new_range.append(new_r)
    return new_range

arr = []
for line in f:
    if line.strip() == "":
        fresh_ranges = arr
        arr = []
        continue
    arr.append(line.strip())
ingredients = arr

for i in range(1):
    fresh_ranges = (main(fresh_ranges))


count = 0
fresh_ranges.sort()
print(fresh_ranges)
for r in fresh_ranges:
    if r is False: continue
    rs,rf = r.split("-")
    s = int(rf)-int(rs)+1
    count = count + s
    print(r+" - > \t" + str(s))
print(count)

#421073057078519