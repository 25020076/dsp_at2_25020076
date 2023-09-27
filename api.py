import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string.

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.status_code, response.json()  # Return status code and JSON content
    except requests.RequestException as e:  # This will catch any type of RequestException (like HTTPError, ConnectionError, Timeout etc.)
        return response.status_code, str(e)  # Return status code and error message
