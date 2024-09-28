from functions import *

production(8,RIG,H2O,1)
production(5,FRM,GRN,1)
production(13,INC,C,1)

print()
housing(11,HB1)
print(f"                 {NEON_CYAN}{sum(pioneers)}{WHITE} total pioneers\n")
housing(0, HB2)
print(f"                 {NEON_CYAN}{sum(settlers)}{WHITE} total settlers\n")

print(f"{NEON_YELLOW}{sum(total_area)} area used.")
print(f"{RED}{500 - sum(total_area)} area left.")

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

print(f"FINAL CALCULATION: {RED}{totalmaterialcost} NCC required.")

