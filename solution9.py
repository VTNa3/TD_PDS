def elec_bill(kwh):

    if kwh < 0:
        return None
    if kwh <= 50:
        t1 = kwh * 480
        t2 = 0
        t3= 0
    elif kwh > 50 and kwh <= 200:
        t1 = 50 * 480
        t2 = (kwh - 50) * 610
        t3 = 0
    else:
        t1 = 50 * 480
        t2 = 150 * 610
        t3 = (kwh - 200) * 730
    subtotal = (t1 + t2 + t3) + 2000
    vat = subtotal * 0.10
    riel = round(subtotal + vat)
    dollars = round(riel / 4100, 2)

    return riel, dollars

    
for k in [ 0, 35, 50, 120, 200, 350 ]:
    bill = elec_bill(k)
    if bill is None:
        print("Invalid Input !")
    else:
        riel, dollars = bill    
        print(f"{k:>5} kWh -> {riel:>8,} Riel (≈{dollars:>7.2f} USD)")

print("\n(c). Ask the user for their monthly consumption and print their bill.\n")

kwh = float(input("Please enter your monthly electricity consumption in kWh: "))
bill = elec_bill(kwh)
if bill is None:
    print("Invalid Input !")
else: 
    riel, dollars = bill
    print(f"Your electricity bill for {kwh} kWh is : {riel} Riel (≈ {dollars:.2f} USD)")