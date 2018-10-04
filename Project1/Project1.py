def get_integer_input(question_to_ask):
    is_invalid_input = True

    while is_invalid_input:
        answer = input(question_to_ask)
        for character in answer:
            if not character.isdigit():
                print("Please enter only numeric values")
                break
        else:
            is_invalid_input = False
    return int(answer)


def get_selection_from_valid_choices(question_to_ask, list_of_valid_choices):
    answer = ""
    while answer not in list_of_valid_choices:
        answer = input(question_to_ask).lower()
    return answer


total_allowances = 1

status = get_selection_from_valid_choices("How are you going to file?"
       "\nSingle"
       "\nMarried"
       "\nHead of Household",
        ("single", 'married', 'head of household'))

spouse_income = 0

if status != "single":
    total_allowances += 1
    if status == "married":
        spouse_works = input("Does your spouse work?")
        if spouse_works == "yes":
            spouse_income = get_integer_input("How much does your spouse earn?")

total_jobs = get_integer_input("How many jobs do you have?")

if total_jobs == 1:
    if status == "single":
        total_allowances += 1
    elif status == "married":
        if spouse_works == "no":
            total_allowances += 1
        elif spouse_income < 1500:
                total_allowances += 1
else:
    other_job_wages = get_integer_input("How much do you make at your other jobs?")

    other_job_wages += spouse_income

    if other_job_wages < 1500:
        total_allowances += 1
total_income = get_integer_input("Please enter your estimated total income")

number_of_children = get_integer_input("How many children do you have?")

if (total_income < 69801 and status == "single") \
        or (total_income < 101401 and status == "married"):
    total_allowances += number_of_children * 4
elif (total_income < 175550 and status == "single") \
        or (total_income < 339000 and status == "married"):
    total_allowances += number_of_children * 2
elif (total_income < 200000 and status == "single") \
        or (total_income < 400000 and status == "married"):
    total_allowances += number_of_children

number_of_other_dependents = int(input("How many children do you have?"))

if (total_income < 69801 and status == "single") \
        or (total_income < 101401 and status == "married"):
    total_allowances += number_of_other_dependents
elif (total_income < 175550 and status == "single") \
        or (total_income < 339000 and status == "married"):
    total_allowances += number_of_other_dependents // 2

other_credits = get_integer_input("Do you have any other credits to add?")

total_allowances += other_credits

itemize = input("Do you want to itemize your deductions?")
if itemize.lower() == 'yes':
    total_deductions = get_integer_input("Enter your estimated total deductions")

    if status == "single":
        total_deductions -= 12000
    elif status == "married":
        total_deductions -= 24000
    elif status == "head of household":
        total_deductions -= 18000

    if total_deductions < 0:
        total_deductions = 0

    other_adjustments = get_integer_input("Other adjustments for age or blindness?")

    total_deductions += other_adjustments

    non_wage_income = get_integer_input("Please enter your non wage income")

    total_deductions -= non_wage_income

    other_deductions = total_deductions // 4150

    total_deductions += other_deductions

print("You should claim %d deductions on your W4" % total_allowances)

