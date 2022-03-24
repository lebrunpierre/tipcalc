def calculate_bill(bill, amount_of_people, tip_percentage):
    """

    :param bill: The bill the party is being billed
    :param amount_of_people: amount of people that will be splitting the bill
    :param tip_percentage: the tip amount that the party wants to leave
    :return: returns the amount each person will have to pay

    This function calculates how much each person must pay after splitting the bill evenly.

    """

    percent = tip_percentage / 100
    total_with_tip = (float(bill) * percent) + bill

    return total_with_tip / amount_of_people


# percentage insures user only uses predefined percentage amounts
percentage = [10, 12, 15]
# Percentage so user can see them.
print_out_percentages = str(percentage).strip('[]')

print('Welcome to the bill calculator!')
bill = float(input('What was the total bill? $'))
amount_of_people = int(input('How many people to split the bill? '))
tip_percentage = float(input(f'What percentage tip would you like to give? {print_out_percentages} '))

# will not proceed until user picks percentage from the list
while tip_percentage not in percentage:
    tip_percentage = int(input(f'Tip percentage must be {print_out_percentages} '))

pay_per_person = calculate_bill(bill, amount_of_people, tip_percentage)

print(f'Each person should pay {pay_per_person}')
