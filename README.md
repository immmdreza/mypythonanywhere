# MyPythonAnywhere

A python async package to communicate with [PythonAnywhere](https://help.pythonanywhere.com/pages/API) api.

## Installation

The beta package is available at [PyPi](https://pypi.org/project/mypythonanywhere).

## Get Started

### Requirements

1. Api Token: get your api token from [pythonanywhere account page](https://www.pythonanywhere.com/user/MerrilleChoate/account/).

2. Determine if your account is US_Based or EU_Based ( It's commonly US. )

3. Your username.

### Create Client

``` py
from mypythonanywhere import AccountType, FriendlyPythonAnywhereClient

client = FriendlyPythonAnywhereClient(
    username='MerrilleChoate',
    token='API_TOKEN',
    account_type=AccountType.UsBased
)
```

### Send Requests

Get cpu usage.

``` py
>>> result = await client.cpu.get_cpu_usage()
>>> print(result)
# CpuUsage(daily_cpu_limit_seconds=100, next_reset_time='2022-04-17T11:23:40', daily_cpu_total_usage_seconds=0.0) 
```

Get all of your consoles.

``` py
>>> result = await client.consoles.get_consoles()
>>> print(result)
# [Console(id=24036640, user='MerrilleChoate', executable='python2.7', arguments='', working_directory=None, name='Python2.7 console 24036640', console_url='/user/MerrilleChoate/consoles/24036640/', console_frame_url='/user/MerrilleChoate/consoles/24036640/frame/')]
```

### A full example

Send requests one by one

``` py
import asyncio

async def main():

    client = FriendlyPythonAnywhereClient(
        username='MerrilleChoate',
        token='API_TOKEN',
        account_type=AccountType.UsBased
    )

    consoles = await client.console.get_consoles()
    print(consoles)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Send a batch of requests using one session

``` py
import asyncio

async def main():

    client = FriendlyPythonAnywhereClient(
        username='MerrilleChoate',
        token='API_TOKEN',
        account_type=AccountType.UsBased
    )

    async with client:
        consoles = await client.console.get_consoles()
        for x in consoles:
            await client.console.kill_console(x.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Direct Call

``` py
from mypythonanywhere.pythonanywhere import PythonAnywhereClient
from mypythonanywhere.types.requests.console_requests import GetConsoleInfo

client = PythonAnywhereClient(
    # --- sniff ---
)

console = await client(GetConsoleInfo(123456789)) # Console
```

🍟 _Not all methods are implemented yet!_
...

## Contribute

There're api methods that are not implemented. following the order of <https://help.pythonanywhere.com/pages/API>, methods related to files and below are yet to implement.

### Implement Methods?

Take a look at [requests dir](src/mypythonanywhere/types/requests) for examples of implementing api methods.

All you need is to inherit from `BaseRequest[T]` ( where `T` is the method return type ). then filling the abstract methods, unless you face something new.

### Automated tests

Tests are missing for most of methods.
