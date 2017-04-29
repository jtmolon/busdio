import requests
import sys

from endpoints import REAL_TIME_ENDPOINT


def get_info(stopid):
    """ Returns real time information for stopid
    """
    params = {'stopid': stopid}
    params['format'] = 'json'
    result = requests.get(REAL_TIME_ENDPOINT, params=params)
    return result.json()


if __name__ == "__main__":
    stopid = sys.argv[1]
    print(get_info(stopid))
