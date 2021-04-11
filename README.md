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
from stock_exchange_holidays import NYSE

calendar = NYSE()
calendar.get_holidays()
calendar.get_holidays_by_year(year=2021)
```

### Chicago Mercantile Exchange (CME)
```python
from stock_exchange_holidays import CME

calendar = CME()
calendar.get_holidays()
calendar.get_holidays_by_year(year=2021)
```

### Sao Paulo Stock exchange (B3) formerly BM&F-BOVESPA
```python
from stock_exchange_holidays import B3
calendar = B3()
calendar.get_holidays()
calendar.get_holidays_by_year(year=2021)
```


## License

MIT
