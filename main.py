from colors import *

FEO = 'FEO'
FE = 'FE'
LST = 'LST'
O = 'O'
C = 'C'
BBH = 'BBH'
FLX = 'FLX'

dict = {
    FEO: [8],
    LST: [11],
    O: [3],
    FE: [4,6,1,1,1],
    BBH: [1,1,2],
    FLX: [10],
}

# ---------------------------

def prodRate(item, building, hrs, mins, cost1=None, cost2=None, cost3=None, cost4=None, days=None, price=None):
    per = dict[item][0]
    exthrs = hrs + mins / 60
    totalprod = per * building

    if days is not None:
        cycles = int(days * 24 / exthrs)
        period = f'in {days} days'
    else:
        cycles = int(168 / exthrs)
        period = 'per week'

    perweek = totalprod * cycles
    cost_str = ''
    
    if cost1 is not None:
        cost_1 = dict[item][1] * cycles * building
        cost_str += f', costing {cost_1} {cost1}'
    if cost2 is not None:
        cost_2 = dict[item][2] * cycles * building
        cost_str += f', {cost_2} {cost2}'
    if cost3 is not None:
        cost_3 = dict[item][3] * cycles * building
        cost_str += f', {cost_3} {cost3}'
    if cost4 is not None:
        cost_4 = dict[item][4] * cycles * building
        cost_str += f', {cost_4} {cost4}'

    if price is not None:
        totalprice = price*perweek
        price_str = f', selling at {totalprice} NCC in total'
    else:
        price_str = ''

    print(f'{item}: {totalprod} every {hrs}h{mins}m, {perweek} {period}{cost_str}{price_str}.\n')

# --------------------------

print("Welcome to the VELLICHOR Accounting Department.")
print("This is Montem.\n")

print(f'\n{BOLD}{ITALIC}Current production/extraction rates:{WHITE}\n')

prodRate(FEO,1,15,58)
prodRate(LST,1,15,54)
prodRate(O,1,8,1)
prodRate(FLX,1,26,0)
prodRate(FE, 3, 16, 33, FEO, C, O, FLX)