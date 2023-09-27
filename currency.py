def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, 4)

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        return round(1 / rate, 4)
    return 0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Format the conversion result into the desired string format.

    Parameters
    ----------
    date: str
        The date of the conversion rate.
    from_currency: str
        The base currency.
    to_currency: str
        The target currency.
    rate: float
        The conversion rate.
    amount: float
        The amount in the base currency.

    Returns
    -------
    str
        The formatted result.
    """
    converted_amount = amount * rate
    inverse_rate = reverse_rate(rate)
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate):.4f}. "
            f"So {amount:.2f} in {from_currency} correspond to {converted_amount:.2f} in {to_currency}. "
            f"The inverse rate was {inverse_rate:.4f}.")
   
