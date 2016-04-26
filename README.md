# Starter Weppy
![BuildStatus](https://travis-ci.org/mijdavis2/starter_weppy.svg?branch=master)

Starter Weppy is a web application starter kit 
built on the [weppy framework](http://weppy.org/). 

TODO: 

- Write a script that will create a new project based on this "starter
weppy" structure with an app name as an argument.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Run](#run)
  - [Docker](#docker)
- [Develop](#develop)
- [Test](#test)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Run

**Requirements**:
- Python 3.5.1

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

### Docker

To make your application available at ```http://localhost/```:

```
docker build -t starter-weppy .
docker run -it -p 80:8000 --rm --name starter-weppy starter-weppy
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

See ```starter_weppy/cli.py``` for cli commands. 

## Test

```
py.test -v -s --cov-report term-missing --cov=starter_weppy -r w tests
```
