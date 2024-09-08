from colors import *
from lists import *

def prodRate(building_count, building,cost1=None, cost2=None, cost3=None, cost4=None):
    pioneers.append(building.get('pioneers', 0) * building_count)
    settlers.append(building.get('settlers', 0) * building_count)

    hrs = building.get('hours')
    mins = building.get('minutes')
    totalprod = building.get('per') * building_count
    item = building.get('item')
    per = building.get('per')

    exthrs = hrs + mins / 60
    totalprod = per * building_count

    cycles = int(168 / exthrs)
    period = 'per week'

    perweek = totalprod * cycles
    cost_str = ''

    if cost1 is not None:
        cost_1 = building.get('cost')[0] * cycles * building_count
        cost_str += f', costing {cost_1} {cost1}'
    if cost2 is not None:
        cost_2 = building.get('cost')[1] * cycles * building_count
        cost_str += f', {cost_2} {cost2}'
    if cost3 is not None:
        cost_3 = building.get('cost')[2] * cycles * building_count
        cost_str += f', {cost_3} {cost3}'
    if cost4 is not None:
        cost_4 = building.get('cost')[3] * cycles * building_count
        cost_str += f', {cost_4} {cost4}'

    construction(building,building_count)
    total_area.append(building.get('area')*building_count)
    print(f'{item}: {building_count} {building.get("name")} * {per} every {hrs}h{mins}m, {NEON_BLUE}{perweek}{WHITE} {period}{cost_str}. Takes up {NEON_YELLOW}{building.get("area")*building_count}{WHITE} area.')

def housing(building_count, building):
    if building == HB1:
        worker = "pioneers"
    elif building == HB2:
        worker = "settlers"

    construction(building,building_count)
    total_area.append(building.get('area')*building_count)
    print(f"{building_count} {building.get('name')}. Space for {NEON_GREEN}{100*building_count}{WHITE} {worker}. Takes up {NEON_YELLOW}{building.get("area")*building_count}{WHITE} area.")

def construction(building,building_count):
    totalBSE.append(building.get("BSE", 0) * building_count)
    totalBBH.append(building.get("BBH", 0) * building_count)
    totalBDE.append(building.get("BDE", 0) * building_count)
    totalMCG.append(building.get("MCG", 0) * building_count)
    totalBTA.append(building.get("BTA", 0) * building_count)
    totalTRU.append(building.get("TRU", 0) * building_count)
    totalLBH.append(building.get("LBH", 0) * building_count)
# --------------------------
pioneers = []
settlers = []
totalBSE = []
totalBBH = []
totalBDE = []
totalMCG = []
totalBTA = []
totalTRU = []
totalLBH = []
total_area = [25]
'''
print()
prodRate(4,COL)
prodRate(30,POL,C,H,CL,O)

print()
housing(6,HB1)
print(f"                 {NEON_CYAN}{sum(pioneers)}{WHITE} total pioneers\n")
housing(8, HB2)
print(f"                 {NEON_CYAN}{sum(settlers)}{WHITE} total settlers\n")

print(f"{NEON_YELLOW}{sum(total_area)} area used.")
print(f"{RED}{750 - sum(total_area)} area left.")

print("\nMaterial Costs:")
print(
    f"{NEON_PURPLE}{sum(totalBSE)}{WHITE} BSE\n"
    f"{NEON_PURPLE}{sum(totalBBH)}{WHITE} BBH\n"
    f"{NEON_PURPLE}{sum(totalBDE)}{WHITE} BDE\n"
    f"{NEON_PURPLE}{sum(totalBTA)}{WHITE} BTA\n"
    f"{NEON_PURPLE}{sum(totalTRU)}{WHITE} TRU\n"
    f"{NEON_PURPLE}{sum(totalMCG)}{WHITE} MCG\n"
    f"{NEON_PURPLE}{sum(totalLBH)}{WHITE} LBH\n"
)

totalmaterialcost = (sum(totalBSE)*1700 +
                     sum(totalBBH)*2500 +
                     sum(totalBDE)*2400 +
                     sum(totalBTA)*1500 +
                     sum(totalTRU)*400 +
                     sum(totalMCG)*40 +
                     sum(totalLBH)*4000)

print(f"FINAL CALCULATION: {RED}{totalmaterialcost} NCC required.")'''