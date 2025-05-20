def calculate_interest_for_periods(amount: float, nominal_rate: float):
    """Calculate interest for different compounding periods using AER industry standard.

    Args:
        amount (float): The principal amount.
        nominal_rate (float): The nominal interest rate (as a decimal).

    Returns:
        dict: A dictionary containing the interest for daily, weekly, monthly, and yearly periods.
    """
    # Define compounding frequencies based on 365.25 days/year
    compounding_frequencies = {
        'Daily': 365,
        'Weekly': 365 / 7,
        'Monthly': 12,
        'Yearly': 1
    }

    interest_data = {}
    for period, freq in compounding_frequencies.items():
        period_rate = (1 + (nominal_rate/100)) ** (1 / freq) - 1
        interest = amount * period_rate
        interest_data[period] = interest

    return interest_data
