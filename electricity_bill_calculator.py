# calculates an electricity bill

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

run = True

while run is True:

    tariff = float(input("Which tariff?"))
    daily_use = float(input("Enter your daily use in kWh:"))
    billing_period = float(input("Enter the number of days in the billing period:"))

    if tariff == 11:
        total_cost = TARIFF_11 * daily_use * billing_period
        run = False
    elif tariff == 31:
        total_cost = TARIFF_31 * daily_use * billing_period
        run = False
    else:
        print("Enter a correct tariff")
print("Your bill is: ", total_cost)