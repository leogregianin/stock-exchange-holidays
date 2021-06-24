# Worldwide Stock Exchange holidays


## Development

### Create virtual environment

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

### Install Dependencies
    
without dependencies

## Using

### New York Stock Exchange (NYSE)
```python
from stock_exchange_holidays import Holidays, NYSE

holidays = Holidays(exchange=NYSE())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```

### Chicago Mercantile Exchange (CME)
```python
from stock_exchange_holidays import Holidays, CME

holidays = Holidays(exchange=CME())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```

### Sao Paulo Stock exchange (B3) formerly BM&F-BOVESPA
```python
from stock_exchange_holidays import Holidays, B3

holidays = Holidays(exchange=B3())
print(holidays.get_holidays())
print(holidays.get_holidays_by_year(year=2021))
```


## License

MIT
