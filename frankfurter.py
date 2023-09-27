from api import get_url

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.
    
    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    url = f"{BASE_URL}/currencies"
    status_code, response_content = get_url(url)
    
    if status_code == 200 and isinstance(response_content, dict):
        return list(response_content.keys())
    else:
        return None


def get_latest_rates(from_currency, to_currency):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.
    
    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    
    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    status_code, response_content = get_url(url)

    if status_code == 200 and "rates" in response_content and to_currency in response_content["rates"]:
        date = response_content.get("date", "")
        rate = response_content["rates"][to_currency]
        return date, rate
    else:
        return None, None

def get_historical_rate(from_currency, to_currency, from_date):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}"
    status_code, response_content = get_url(url)

    if status_code == 200 and "rates" in response_content and to_currency in response_content["rates"]:
        return response_content["rates"][to_currency]
    else:
        return None