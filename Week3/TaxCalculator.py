taxes_owed_at_10_percent = 0
taxes_owed_at_12_percent = 0
taxes_owed_at_22_percent = 0
taxes_owed_at_24_percent = 0
taxes_owed_at_32_percent = 0
taxes_owed_at_35_percent = 0
taxes_owed_at_37_percent = 0

filing_status = input("Are you filing single or married? ")

income = int(
    input("Please enter your total income for 2018"))


# gets the first letter
if filing_status.lower()[0] == "s":
    TOP_OF_10_BRACKET = 9525
    TOP_OF_12_BRACKET = 38700
    TOP_OF_22_BRACKET = 82500
    TOP_OF_24_BRACKET = 157500
    TOP_OF_32_BRACKET = 200000
    TOP_OF_35_BRACKET = 500000
    standard_deduction = 12000

else:
    TOP_OF_10_BRACKET = 19050
    TOP_OF_12_BRACKET = 77400
    TOP_OF_22_BRACKET = 165000
    TOP_OF_24_BRACKET = 315000
    TOP_OF_32_BRACKET = 400000
    TOP_OF_35_BRACKET = 600000
    standard_deduction = 24000

use_standard_deduction = input("Do you want to use the standard deduction ($" + str(standard_deduction) + ")")

TAX_RATES = {
    "10%": .1,
    "12%": .12,
    "22%": .22,
    "24%": .24,
    "32%": .32,
    "35%": .35,
    "37%": .37}


if use_standard_deduction.lower()[0] == "y":
    income -= standard_deduction
else:
    total_deductions = int(input("Enter your total deductions: "))
    income -= total_deductions

if income <= TOP_OF_10_BRACKET:
    taxes_owed_at_10_percent = income * TAX_RATES["10%"]

elif income <= TOP_OF_12_BRACKET:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (income - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

elif income <= TOP_OF_22_BRACKET:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (TOP_OF_12_BRACKET - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

    taxes_owed_at_22_percent = \
        (income - TOP_OF_12_BRACKET) * TAX_RATES["22%"]

elif income <= TOP_OF_24_BRACKET:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (TOP_OF_12_BRACKET - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

    taxes_owed_at_22_percent = \
        (TOP_OF_22_BRACKET - TOP_OF_12_BRACKET) * TAX_RATES["22%"]

    taxes_owed_at_24_percent = \
        (income - TOP_OF_22_BRACKET) * TAX_RATES["24%"]

elif income <= TOP_OF_32_BRACKET:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (TOP_OF_12_BRACKET - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

    taxes_owed_at_22_percent = \
        (TOP_OF_22_BRACKET - TOP_OF_12_BRACKET) * TAX_RATES["22%"]

    taxes_owed_at_24_percent = \
        (TOP_OF_24_BRACKET - TOP_OF_22_BRACKET) * TAX_RATES["24%"]

    taxes_owed_at_32_percent = \
        (income - TOP_OF_24_BRACKET) * TAX_RATES["32%"]

elif income <= TOP_OF_35_BRACKET:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (TOP_OF_12_BRACKET - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

    taxes_owed_at_22_percent = \
        (TOP_OF_22_BRACKET - TOP_OF_12_BRACKET) * TAX_RATES["22%"]

    taxes_owed_at_24_percent = \
        (TOP_OF_24_BRACKET - TOP_OF_22_BRACKET) * TAX_RATES["24%"]

    taxes_owed_at_32_percent = \
        (TOP_OF_32_BRACKET - TOP_OF_24_BRACKET) * TAX_RATES["32%"]

    taxes_owed_at_35_percent = \
        (income - TOP_OF_32_BRACKET) * TAX_RATES["35%"]

else:
    taxes_owed_at_10_percent = \
        TOP_OF_10_BRACKET * TAX_RATES["10%"]

    taxes_owed_at_12_percent = \
        (TOP_OF_12_BRACKET - TOP_OF_10_BRACKET) * TAX_RATES["12%"]

    taxes_owed_at_22_percent = \
        (TOP_OF_22_BRACKET - TOP_OF_12_BRACKET) * TAX_RATES["22%"]

    taxes_owed_at_24_percent = \
        (TOP_OF_24_BRACKET - TOP_OF_22_BRACKET) * TAX_RATES["24%"]

    taxes_owed_at_32_percent = \
        (TOP_OF_32_BRACKET - TOP_OF_24_BRACKET) * TAX_RATES["32%"]

    taxes_owed_at_35_percent = \
        (TOP_OF_35_BRACKET - TOP_OF_32_BRACKET) * TAX_RATES["35%"]

    taxes_owed_at_37_percent = \
        (income - TOP_OF_35_BRACKET) * TAX_RATES["37%"]

print("Taxes owed at 10%%: $%.2f" % taxes_owed_at_10_percent)
print("Taxes owed at 12%%: $%.2f" % taxes_owed_at_12_percent)
print("Taxes owed at 22%%: $%.2f" % taxes_owed_at_22_percent)
print("Taxes owed at 24%%: $%.2f" % taxes_owed_at_24_percent)
print("Taxes owed at 32%%: $%.2f" % taxes_owed_at_32_percent)
print("Taxes owed at 35%%: $%.2f" % taxes_owed_at_35_percent)
print("Taxes owed at 37%%: $%.2f" % taxes_owed_at_37_percent)

total_taxes = taxes_owed_at_10_percent + \
            taxes_owed_at_12_percent + \
            taxes_owed_at_22_percent + \
            taxes_owed_at_24_percent + \
            taxes_owed_at_32_percent + \
            taxes_owed_at_35_percent + \
            taxes_owed_at_37_percent

print("Total taxes: $%.2f" % total_taxes)


print("Taxes as percentage of income: %.2f %%"
      % (total_taxes / income * 100 ))
