from colors import *
from buildings import *
from production import *

#ORDER SIZE

pioneers = []
settlers = []
totalBSE = []
totalBBH = []
totalBDE = []
totalMCG = []
totalBTA = []
totalTRU = []
totalLBH = []

total_C = []
total_H = []
total_MG = []
total_CL = []

total_area = [25]


def production(building_count, building, item, order_size = None):
    pioneers.append(building.get('pioneers', 0) * building_count)
    settlers.append(building.get('settlers', 0) * building_count)

    if order_size is not None:
        order_size_var = order_size
    else:
        order_size_var = 1

    hrs = item.get('hours')
    mins = item.get('minutes')
    per = item.get('per')
    percycle = item.get('per') * building_count * order_size_var
    itemname = item.get('name')

    cyclehours = hrs + mins / 60
    cyclesperweek = int(168 / cyclehours)
    perweek = percycle * cyclesperweek

    input_str = ''
    inputs_list = []
    total_costs = 0  # Initialize total costs for all inputs

    if item.get('costs') is not None:
        input_str = ', costing '

        for key, value in item['costs'].items():
            if isinstance(value, dict):  # Check if the value is a dictionary with 'amount' and 'price'
                inputperweek = value['amount'] * building_count * cyclesperweek * order_size_var
                inputs_list.append(f"{RED}{inputperweek}{WHITE} {key}")
                total_costs += value['price'] * inputperweek  # Sum the total cost for each input
            else:  # If it's an integer, use it directly (as 'amount')
                inputperweek = value * building_count * cyclesperweek
                inputs_list.append(f"{RED}{inputperweek}{WHITE} {key}")

        final_inputs = ', '.join(inputs_list)
        result = input_str + final_inputs
    else:
        result = ''

    # Calculate weekly revenue and profit
    if item.get('price') is not None:
        weeklyrevenue = item.get('price') * perweek
        weeklycosts = total_costs
        profit = weeklyrevenue - weeklycosts
        profit_str = f'\n{NEON_GREEN}{weeklyrevenue}{WHITE} NCC - {RED}{weeklycosts}{WHITE} NCC = {NEON_GREEN}{profit}{WHITE} NCC profit'
    else:
        profit_str = ''

    construction(building, building_count)
    total_area.append(building.get('area') * building_count)

    # Print the final production and profit details
    print(
        f'{itemname}: {building_count} {building.get("name")} * {per} every {hrs}h{mins}m, {NEON_BLUE}{perweek}{WHITE} per week{result}. '
        f'Takes up {NEON_YELLOW}{building.get("area") * building_count}{WHITE} area.{profit_str}')


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