"""pizza order code """
small = 10
medium = 15
large = 20
pep_for_small = 2
pep_for_medium_or_large = 3
extra_cheese = 1
total_amount = 0


def calculate_price(price):
    global total_amount
    total_amount += price
    resp = input("Would you like extra cheese?")
    if resp.lower() == "yes":
        total_amount += extra_cheese
    else:
        pass
    resp2 = input("Would you like extra pepperoni?")
    if resp2.lower() == "yes":
        total_amount += pep_for_medium_or_large
    else:
        pass
    print("Your total fee is: ", total_amount)


while True:
    print("What type pizza dou you want?")
    size = input("size:")
    if size.lower() == "small":
        total_amount += 10
        resp = input("Dou you want extra cheese?")
        if resp.lower() == "yes":
            total_amount += extra_cheese
        else:
            pass
        resp2 = input("Dou you want extra pepperoni?")
        if resp2.lower() == "yes":
            total_amount += pep_for_small
        else:
            pass
        print("Your total fee is: ", total_amount)
        total_amount = 0
    elif size.lower() == "medium":
        calculate_price(medium)
        total_amount = 0
    elif size.lower() == "large":
        calculate_price(large)
        total_amount = 0
    else:
        print("This size is invalid for system")
