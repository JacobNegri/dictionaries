# calculates an electricity bill

TARIFF = {11: 0.244618, 31: 0.136928}

run = True

while run is True:

    tariff = int(input("Which tariff?"))
    daily_use = float(input("Enter your daily use in kWh:"))
    billing_period = int(input("Enter the number of days in the billing period:"))

    if tariff in TARIFF:
        tariff_price = TARIFF[tariff]
        total_cost = tariff_price * daily_use * billing_period
        run = False
    else:
        print("Enter a correct tariff")

print("Your bill is: $", total_cost)