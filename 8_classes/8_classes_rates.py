import requests
from libs.exchange import Rate
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_max_rate_name():
    max_rates = Rate()
    max_rate_name = ''
    max_rate_value = 0
    for i in max_rates.exchange_rates().values():
        if i['Value'] >= max_rate_value:
            max_rate_name = i['Name']
    return max_rate_name


print(get_max_rate_name())

test = Rate(diff=True)
print(test.eur())

