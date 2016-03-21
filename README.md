# Starter Weppy

Starter Weppy is an experimental baseline microservice application
starter kit built on the [weppy framework](http://weppy.org/). 

TODO: 

- Write a script that will create a new project based on this "starter
weppy" structure with an app name as an argument.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Run](#run)
- [Develop](#develop)
- [Test](#test)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Run

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


## Develop

Running in development mode will enable debug pages,
automatically create test, users in multiple states,
and upon killing the app, those test users will automatically be 
deleted from the DB.

To start the app in development mode, do:

```
python run.py --dev
```

See ```my_weppy_app_/cli.py``` for cli commands. 

## Test

The tests requires the app to be running in dev mode for integration
testing.

Run the app in dev mode. Then in another shell, do:

```
py.test -v -s --cov-report term-missing --cov=my_weppy_app tests
```
