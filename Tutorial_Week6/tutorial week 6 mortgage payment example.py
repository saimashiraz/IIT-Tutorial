def main():
    # 1) Get inputs from the user (as numbers).
    annual_interest_rate, monthly_payments, beginning_month_balance = input_data()

    # 2) Do the math to compute interest paid for the month, reduction of principal, and end of month balance.
    monthly_interest_paid, reduction_of_principal, month_end_balance = calculate_the_values(annual_interest_rate, monthly_payments, beginning_month_balance)

    # 3) Show the results nicely formatted (two decimals, with $).
    display_new_data(monthly_interest_paid, reduction_of_principal, month_end_balance)


def input_data():
    """
    This function is a little 'machine' that ONLY asks for input.
    It returns three numbers that other functions will use.
    - annual interest rate: the interest rate applied to your annual mortgage payment
    - monthly payments: the set amount of mortgage you have to pay each month
    - beginning month balance: the total amount that you owe at th ebeginning of eah month
    """
    # input(...) shows a message and waits for the user to type something.
    # float(...) converts the typed text into a decimal number like 123.45
    annual_interest_rate    = float(input("Enter annual rate of interest: “))
    monthly_payments        = float(input("Enter monthly payment: “))
    beginning_month_balance = float(input("Enter beginning of month balance: “))

    # Return all three results at once as a "tuple".
    return annual_interest_rate, monthly_payments, beginning_month_balance



def calculate_new_values(annual_interest_rate, monthly_payments, beginning_month_balance):
    """
    This function ONLY does the math.
    Step by step idea (paper version):
      1) Start from beginning_month_balance and add 0.4167% interest -> multiply old balance by 1.004167 
      2) Add this month's charges
      3) Subtract credits (payments/refunds)
      4) Use the minimum payment rule
    """
    # 1.5% interest on the OLD balance means multiplying by 1.015
    new_balance = 1.015 * old_balance + charges - credits

    # Minimum payment rule:
    # - If new_balance is small (<= 20), pay it all.
    # - Otherwise, pay $20 + 10% of the amount above $20.
    if new_balance <= 20:
        minimum_payment = new_balance
    else:
        minimum_payment = 20 + 0.10 * (new_balance - 20)

    # Give both numbers back to whoever called this function.
    return new_balance, minimum_payment
