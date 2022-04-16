# MyPythonAnywhere

A python package to communicate with [PythonAnywhere](https://help.pythonanywhere.com/pages/API) api.

## Installation

The beta package is available at [PyPi](https://pypi.org/project/mypythonanywhere).

## Get Started

### Requirements

1. Api Token: get your api token from [pythonanywhere account page](https://www.pythonanywhere.com/user/MerrilleChoate/account/).

2. Determine if your account is US_Based or EU_Based ( It's commonly US. )

3. Your username.

### Create Client

``` py
from mypythonanywhere import PythonAnywhereClient, AccountType

client = PythonAnywhereClient(
    username='MerrilleChoate',
    token='API_TOKEN',
    account_type=AccountType.UsBased
)
```

### Send Requests

Get cpu usage.

``` py
>>> result = client.cpu.get_cpu_usage()
>>> print(result)
# CpuUsage(daily_cpu_limit_seconds=100, next_reset_time='2022-04-17T11:23:40', daily_cpu_total_usage_seconds=0.0) 
```

Get all of your consoles.

``` py
>>> result = client.consoles.get_consoles()
>>> print(result)
# [Console(id=24036640, user='MerrilleChoate', executable='python2.7', arguments='', working_directory=None, name='Python2.7 console 24036640', console_url='/user/MerrilleChoate/consoles/24036640/', console_frame_url='/user/MerrilleChoate/consoles/24036640/frame/')]
```

### Direct Call

``` py
from mypythonanywhere.types.requests.console_requests import GetConsoleInfo

# --- sniff ---

console = client(GetConsoleInfo(123456789)) # Console
```

🍟 _Not all methods are implemented yet!_
...
