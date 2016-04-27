# Starter Weppy
[![Build Status](https://travis-ci.org/mijdavis2/starter_weppy.svg?branch=master)](https://travis-ci.org/mijdavis2/starter_weppy)
[![Coverage Status](https://coveralls.io/repos/github/mijdavis2/starter_weppy/badge.svg?branch=master)](https://coveralls.io/github/mijdavis2/starter_weppy?branch=master)

Starter Weppy is a web application starter kit 
built on the [weppy framework](http://weppy.org/). 

TODO:
- Complete yeoman generator at [https://github.com/mijdavis2/generator-weppy-mvc](https://github.com/mijdavis2/generator-weppy-mvc)


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


## License

MIT © [mijdavis2](http://mdavisinsc.com)
