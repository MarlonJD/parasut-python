[![codecov](https://codecov.io/gh/MarlonJD/parasut-python/branch/master/graph/badge.svg?token=7SZMQENJDP)](https://codecov.io/gh/MarlonJD/parasut-python) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) ![PyPI - Downloads](https://img.shields.io/pypi/dm/parasut-python) ![PyPI - License](https://img.shields.io/pypi/l/parasut-python)


parasut-python
==========================
Parasut Python API Wrapper (Unoffical)

## Warning
This project is not offical library. It's unoffical python wrapper
This project is under heavy development. Please be aware before use
Query parameters not included for functions

## Install
```
pip install parasut-python
```


## Using
```
import os
from parasut.client import Client

CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
USERNAME = os.environ['PARASUT_USERNAME']
PASSWORD = os.environ['PARASUT_PASSWORD']

# Remove sandbox=True when production.
# It's activating sandbox urls for testing
# Sandbox link: api.heroku-staging.parasut.com
client_obj = Client(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    username=USERNAME,
                    password=PASSWORD,
                    sandbox=True)

# It's required
client_obj.initialize()

# You can get request parameters from
# https://apidocs.parasut.com/#operation/createContact
# All required request data examples can be found at
# https://apidocs.parasut.com
data = {
    "data": {
      "type": "contacts",
      "attributes": {
        "email": "user@example.com",
        "name": "string",
        "short_name": "string",
        "contact_type": "person",
        "tax_office": "string",
        "tax_number": "string",
        "district": "string",
        "city": "string",
        "address": "string",
        "phone": "string",
        "fax": "string",
        "is_abroad": True,
        "archived": True,
        "iban": "string",
        "account_type": "customer"
      },
      "relationships": {
        "category": {
          "data": {
            "type": "item_categories"
          }
        },
        "contact_people": {
          "data": [
            {
              "type": "contact_people",
              "attributes": {
                "name": "string",
                "email": "user@example.com",
                "phone": "string",
                "notes": "string"
              }
            }
          ]
        }
      }
    }
  }

obj = client_obj.functions.createContact(data)
print(obj.json())
```

## Package

Basic structure of package is

```
├── .gitignore
├── .travis.yml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── parasut
│   ├── __init__.py
│   ├── client.py
│   ├── functions.py
│   ├── urls.py
│   └── version.py
├── pytest.ini
├── requirements.txt
├── script
│   └── test
├── setup.py
└── tests
    ├── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── my_helper.py
    ├── tests_helper.py
    └── unit
        ├── __init__.py
        ├── test_example.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.

## License
MIT, Copyright (c) 2020 Burak Karahan
