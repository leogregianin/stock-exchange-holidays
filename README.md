# Worldwide Stock Exchange holidays

[![PyPI](https://img.shields.io/pypi/v/stock_exchange_holidays)](https://pypi.org/project/stock_exchange_holidays/)[![stock-exchange-holidays](https://github.com/leogregianin/stock-exchange-holidays/actions/workflows/main.yml/badge.svg)](https://github.com/leogregianin/stock-exchange-holidays/actions/workflows/main.yml)[![codecov](https://codecov.io/gh/leogregianin/stock-exchange-holidays/branch/main/graph/badge.svg)](https://codecov.io/gh/leogregianin/stock-exchange-holidays)


## Install

```sh
$ python setup.py install
```


## Development

### Create virtual environment

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

### Install development dependencies
    
```sh
$ pip install -r requirements-dev.txt
```

### Run tests
    
```sh
$ python -m unittest
```


## Using

### New York Stock Exchange (NYSE)
```python
from stock.stock_exchange_holidays import Holidays, NYSE

holidays = Holidays(exchange=NYSE())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```

##### Is specific date holiday in NYSE?

```python
from datetime import date
from stock.stock_exchange_holidays import Holidays, NYSE

first_day = date(2020, 1, 1)
holidays = Holidays(exchange=NYSE())
holidays.is_date_holiday(first_day)
```

### Chicago Mercantile Exchange (CME)
```python
from stock.stock_exchange_holidays import Holidays, CME

holidays = Holidays(exchange=CME())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```

##### Is specific date holiday in CME?

```python
from datetime import date
from stock.stock_exchange_holidays import Holidays, CME

first_day = date(2020, 1, 1)
holidays = Holidays(exchange=CME())
holidays.is_date_holiday(first_day)
```


### Sao Paulo Stock exchange (B3) formerly BM&F-BOVESPA
```python
from stock.stock_exchange_holidays import Holidays, B3

holidays = Holidays(exchange=B3())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```

##### Is specific date holiday in B3?

```python
from datetime import date
from stock.stock_exchange_holidays import Holidays, B3

first_day = date(2020, 1, 1)
holidays = Holidays(exchange=B3())
holidays.is_date_holiday(first_day)
```


## License

MIT
