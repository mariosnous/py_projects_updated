def main():
    print("Monthly payment loan calc")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the interest rate %: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr/1200
    months = years * 12
    monthly_payment = round(principal * monthly_interest_rate /
                            (1-(1 + monthly_interest_rate) ** (-months)))
    print(f"The monthly payment for the loan is:  {monthly_payment}")


main()
