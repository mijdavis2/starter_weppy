# Heliosphere

Heliosphere is an experimental microservice built on the
[weppy framework](http://weppy.org/).


- [How to use it](#how-to-use-it)
- [Test](#test)


## How to use it?

Requirements:
- Python 2.7.11

For automated pip and virtual env setup and creation, 
clone this repository and in your terminal do:

```
. ./setup.sh
python run.py
```

Otherwise, do:

```
pip install -r requirements.txt
python run.py
```

## Test

Run:

```
py.test --cov=heliosphere tests
```