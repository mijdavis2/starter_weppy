# starter_weppy

Starter_weppy is an experimental baseline microservice application
starter kit built on the [weppy framework](http://weppy.org/). 
It's app name is "heliosphere", which one could say is ironic for a microservice. 

TODO: 

- Write a script that will create a project based on this "starter
weppy" structure with an app name as an argument.
- In said script, allow for certain "modules" to be included.

TOC:

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